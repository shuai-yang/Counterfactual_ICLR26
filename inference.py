import json
import os
import re
import argparse
import time
import base64

from g4f.client import Client
#import g4f
from load_datasets import load_all_datasets
from misc.Counterfactual_NeurIPS_2025.prompt import get_prompt

import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image
from transformers import pipeline  # Use a pipeline as a high-level helper

def run_inference(models, dataset, mode, debug=True):
    client = Client()        
    for model in models:
        print("model:", model)
        counter = 1
        llm_responses = {}
        
        if dataset_name == 'CRASS':
            for record in dataset[:30]:  
                input_text = record["input"] 
                answers = list(record["target_scores"].keys())

                prompt = str(get_prompt(dataset_name, mode)).format(
                    premise = input_text.split(".")[0].strip() + ".",
                    qcc = input_text.split(".")[1].strip(),
                    answer1 = answers[0],
                    answer2 = answers[1],
                    answer3 = answers[2],
                    answer4 = answers[3]
                )

                try:
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                    )

                    response_content = response.choices[0].message.content.strip()
                    
                    # Remove the unwanted [[Login to OpenAI ChatGPT]]() part
                    cleaned_content = re.sub(r'\[\[Login to OpenAI ChatGPT\]\]\(\)\s*', '', response_content)
                    # Extract the answer number and explanation
                    match = re.search(r'^\s*(\d)\s*\n(.*)', cleaned_content, re.DOTALL)

                    if match:
                        llm_answer = match.group(1).strip()
                        llm_answer_explanation = match.group(2).strip()
            
                    llm_responses[input_text] = { 
                        "llm_answer": llm_answer, 
                        "llm_answer_explanation": llm_answer_explanation 
                    }
                    
                    # Add a small delay to avoid rate limiting
                    time.sleep(1)

                    print(f"record{counter} done")
                    counter += 1
                    
                except Exception as e:
                    continue

        if 'CVQA' in dataset_name:
            image_names = list(dataset.keys())
            image_folder = f"./data/{dataset_name}/real_images"
            
            for image_name in image_names[:30]:                       
                image_path = f"{image_folder}/{image_name}"
                fact_query = dataset[image_name]['query']
                counter_query = dataset[image_name]['new query']
                image = Image.open(image_path)
                with open(image_path, "rb") as image_file:
                    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

                prompt = str(get_prompt(dataset_name, mode)).format(
                    fact_query = fact_query,
                    counter_query = counter_query,
                    image_path = image_path
                )
                # print(prompt)
                if 'llava' not in model :                                      
                    try:
                        response =  Client().chat.completions.create(
                            model= model,  
                            # meassage=["role": "user", "content": prompt, "image_path": image_path]
                            messages=[
                                {"role": "user", "content": prompt},
                                {"role": "user", "content": f"data:image/jpeg;base64,{base64_image}"}
                            ]
                            # Add any other necessary parameters
                        )
                        response_content = response.choices[0].message.content.strip()
                        print(response_content)
                        #if 'cannot view images' in response_content: 
                        #    print(f'{model} cannot view image {image_name}')
                    
                        fact_answer = None
                        llm_answer = None
                        llm_answer_explanation = None
                        # Match answers and explanations
                        # Use regex to extract the answer and explanation

                        match_q1 = re.search(r"\*\*Answer to Question 1:\*\*\s*(\w+)", response_content, re.IGNORECASE)
                        match_q2 = re.search(r"\*\*Answer to Question 2:\*\*\s*(\w+)", response_content, re.IGNORECASE)
                        match_explanation = re.search(r"\*\*Explanation:\*\*\s*(.*)", response_content, re.DOTALL | re.IGNORECASE)
                        
                        if match_q1:
                            fact_answer = match_q1.group(1)
                        if match_q2:
                            llm_answer = match_q2.group(1)
                        if match_explanation:
                            llm_answer_explanation = match_explanation.group(1).strip()
                    
                        llm_responses[image_name] = {
                            "fact_answer": fact_answer,
                            "llm_answer": llm_answer,
                            "llm_answer_explanation": llm_answer_explanation
                        } 
                        print(llm_responses[image_name])

                        # Add a small delay to avoid rate limiting
                        time.sleep(1)

                        print(f"record{counter} done")
                        counter += 1

                    except Exception as e:
                        print(f"Error: {str(e)}")
                        continue
                    except:
                        continue
                    '''
                    if response is not None and
                        'sorry' not in response and
                        'cannot' not in response  and
                        'rate limit' not in response and
                        "can't" not in response and
                        'not safe' not in response and
                        "don't know" not in response and
                        "403 Forbidden" not in response and
                        'invisible' not in response and
                        'try unlimited chat' not in response and 
                        len(response) > 0:
                            return response
                    else: 
                        print('-'*100)
                        print(response)
                        print('-'*100)
                    '''
                elif 'llava' in model:
                    # Load model and processor
                    model_name = f"llava-hf/{model}"   
                    processor = AutoProcessor.from_pretrained(model_name, use_fast=True, legacy=False, trust_remote_code=True)

                    model_path = f"../huggingface/{model}"    # run program at ~/counterfactual

                    # Load the correct model class for vision-text
                    device = "cuda" if torch.cuda.is_available() else "cpu"
                    pipe = pipeline("image-text-to-text", model=model_path, model_kwargs={"torch_dtype": torch.bfloat16},
                                processor = processor, device=device,) # device=0
                    #pipe = pipeline("image-text-to-text", model=model_path, model_kwargs={"torch_dtype": torch.bfloat16},
                    #             device_map="auto",) # device=0

                    messages = [{
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image", "image": image_path},
                            ],
                        },
                    ]
                    
                    prompt = processor.apply_chat_template(messages, add_generation_prompt=True) #  trust_remote_code=True
                    outputs = pipe(text=messages, max_new_tokens=60, return_full_text=False) #  trust_remote_code=True
                    response_content = str(outputs[0]['generated_text'])
      
                    fact_answer = None
                    llm_answer = None
                    llm_answer_explanation = None
                    # Match answers and explanations
                    match_q1 = re.search(r"\*\*Answer to Question 1:\*\*\s*(\w+)", response_content, re.IGNORECASE)
                    match_q2 = re.search(r"\*\*Answer to Question 2:\*\*\s*(\w+)", response_content, re.IGNORECASE)
                    match_explanation = re.search(r"Explanation:\*\*\s*(.*)", response_content, re.DOTALL | re.IGNORECASE)
                    
                    if match_q1:
                        fact_answer = match_q1.group(1)
                    if match_q2:
                        llm_answer = match_q2.group(1)
                    if match_explanation:
                        llm_answer_explanation = match_explanation.group(1).strip()
                    
                    llm_responses[image_name] = {
                        "fact_answer": fact_answer,
                        "llm_answer": llm_answer,
                        "llm_answer_explanation": llm_answer_explanation
                    } 
                    
                    # Add a small delay to avoid rate limiting
                    time.sleep(1)

                    print(f"record{counter} done")
                    counter += 1
        
        if dataset_name == 'COCO':  # top 30 samples as ground truth
            ids = list(dataset.keys())
            image_folder = f"./data/{dataset_name}/real_images"
            for id in ids[:30]:       
                fact_image_name = dataset[id]['fact_image_name']
                fact_image_path = f"{image_folder}/{fact_image_name}.jpg"
                with open(fact_image_path, "rb") as image_file:
                    base64_fact_image = base64.b64encode(image_file.read()).decode('utf-8')
                fact_caption = dataset[id]['fact_caption']

                counter_image_name = dataset[id]['counter_image_name']
                counter_image_path = f"{image_folder}/{counter_image_name}.jpg"
                with open(counter_image_path, "rb") as image_file:
                    base64_counter_image = base64.b64encode(image_file.read()).decode('utf-8')
                counter_caption = dataset[id]['counter_caption']

                prompt = str(get_prompt(dataset_name, mode)).format(
                    fact_image = fact_image_path,
                    fact_caption = fact_caption,
                    counter_image = counter_image_path,
                    counter_caption = counter_caption,
                )
                
                if 'llava' not in model:
                    try:
                        response =  Client().chat.completions.create(
                            model= model,  
                            messages=[
                                {"role": "user", "content": prompt},
                                {"role": "user", "content": f"data:image/jpg;base64,{base64_fact_image}"},
                                {"role": "user", "content": f"data:image/jpg;base64,{base64_counter_image}"}
                            ]
                        )
                        response_content = response.choices[0].message.content.strip()
                        if 'If you need assistance with this image' in response_content:
                            continue
                        print(response_content)
                        match = re.search(r"\*\*Answer to Question:\s*(yes|no)\*\*", response_content, re.IGNORECASE)
                        match_explanation = re.search(r"\*\*Explanation:\s*(.*)", response_content, re.IGNORECASE)
                    
                        '''
                        if match:
                            llm_answer = match.group(1)
                        if match_explanation:
                            llm_answer_explanation = match_explanation.group(1).strip()
                        '''
                        llm_responses[id] = {
                            "llm_answer": match.group(1).strip().lower() if match else None,
                            "llm_explanation": match_explanation.group(1).strip() if match_explanation else None
                        } 
                        print(llm_responses[id])
                        time.sleep(1)

                        print(f"record{counter} done")
                        counter += 1
                       
                    except Exception as e:
                        print(f"Error processing id {id}: {str(e)}")
                        continue
                
                elif 'llava' in model:
                    # Load model and processor class for vision-text
                    model_name = f"llava-hf/{model}"   
                    model_path = f"../huggingface/{model}"    # run program at ~/counterfactual
                    processor = AutoProcessor.from_pretrained(model_name, use_fast=True, legacy=False, trust_remote_code=True)

                    device = "cuda" if torch.cuda.is_available() else "cpu"
                    pipe = pipeline("image-text-to-text", model=model_path, model_kwargs={"torch_dtype": torch.bfloat16},
                                processor = processor, device=device,) 

                    messages = [{
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image", "image": fact_image_path},
                            {"type": "image", "image": counter_image_path},
                            ],
                        },
                    ]
                    
                    prompt = processor.apply_chat_template(messages, add_generation_prompt=True) 
                    outputs = pipe(text=messages, max_new_tokens=60, return_full_text=False) 
                    response_content = str(outputs[0]['generated_text'])

                    llm_answer = None
                    llm_explanation = None
                    llm_answer= response_content.strip()
                    '''
                    llm_answer = None
                    llm_explanation = None
                    match = re.search(r"Answer to Question:", response_content, re.IGNORECASE)
                    match_explanation = re.search(r"Explanation:", response_content, re.DOTALL | re.IGNORECASE)
                    if match:
                        llm_answer = match.group(1)
                    if match_explanation:
                        llm_explanation = match_explanation.group(1).strip()
                    '''
                    llm_responses[id] = {
                        "llm_answer": llm_answer,
                        "llm_explanation": llm_explanation
                    } 

                    # Add a small delay to avoid rate limiting
                    time.sleep(1)

                    print(f"record{counter} done")
                    counter += 1  
                    
        if 'Arithmetic' in dataset_name:
            for record in dataset[:30]:  
                num1 = record["num1"] 
                num2 = record["num2"] 
                
                prompt = str(get_prompt(dataset_name, mode)).format(
                    num1 = num1,
                    num2 = num2
                )
                
                try:
                    #response = g4f.ChatCompletion.create(
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    
                    response_content = response.choices[0].message.content.strip()
                    #response_content = response.strip()
                    
                    # Remove the unwanted [[Login to OpenAI ChatGPT]]() part
                    cleaned_content = re.sub(r'\[\[Login to OpenAI ChatGPT\]\]\(\)\s*', '', response_content)
                    #print(cleaned_content)
                    llm_answer = None
                    llm_explanation = None
                    # Match answers and explanations
                    match_answer = re.search(r"\*\*Answer to Question:\s*(\w+)\*\*", response_content, re.IGNORECASE)
                    match_explanation = re.search(r"\*\*Explanation:\s*(.*)", response_content, re.DOTALL | re.IGNORECASE)
   
                    if match_answer:
                        llm_answer = match_answer.group(1).strip()
                    if match_explanation:
                        llm_explanation = match_explanation.group(1).strip()
                    llm_responses[num1+"+"+num2] = { 
                        "llm_answer": llm_answer, 
                        "llm_explanation": llm_explanation 
                    }
                    print(llm_responses[num1+"+"+num2])
                    # Add a small delay to avoid rate limiting
                    time.sleep(1)
                    
                    print(f"record{counter} done")
                    counter += 1

                except Exception as e:
                    continue

        if dataset_name == 'CLOMO':
            for key, record in list(dataset.items())[:30]:
                record_id = key if isinstance(key, str) else key[0]  # handle tuple keys like ('train_4578', {...})
                prompt = str(get_prompt(dataset_name, mode)).format(
                    instruction =  record["instruction"],
                    task = record["task"],
                    argument = record["argument"],
                    premise1 = record["premise1"],
                    premise2 = record["premise2"]
                )
                try:
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    response_content = response.choices[0].message.content.strip()
                    # Remove the unwanted [[Login to OpenAI ChatGPT]]() part
                    cleaned_content = re.sub(r'\[\[Login to OpenAI ChatGPT\]\]\(\)\s*', '', response_content)
                    # print(cleaned_content)
                    llm_answer = None
                    llm_explanation = None
                    match_answer = re.search(r"\*\*Modified Argument:\*\*\s*(.*?)(?=\n\*\*Explanation:|\Z)",cleaned_content, re.DOTALL | re.IGNORECASE)
                    match_explanation = re.search(r"\*\*Explanation:\*\*\s*(.*)", cleaned_content, re.DOTALL | re.IGNORECASE)
                    if match_answer:
                        llm_answer = match_answer.group(1).strip()
                    if match_explanation:
                        llm_explanation = match_explanation.group(1).strip()
            
                    llm_responses[record_id] = { 
                        "llm_answer": llm_answer, 
                        "llm_explanation": llm_explanation 
                    }
                    print(llm_responses[record_id])
                    # Add a small delay to avoid rate limiting
                    time.sleep(1)

                    print(f"record{counter} done")
                    counter += 1
                except Exception as e:
                    continue
        if dataset_name == 'Code-Exe':
            ids = list(dataset.keys())
            for id in ids[:30]:  
                instruction = dataset[id]["instruction"]
                input = dataset[id]["input"] 

                prompt = str(get_prompt(dataset_name, mode)).format(
                    instruction = instruction.strip(),
                    input = input.strip()
                )
                
                try:
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                    )

                    response_content = response.choices[0].message.content.strip()
                    
                    # Remove the unwanted [[Login to OpenAI ChatGPT]]() part
                    cleaned_content = re.sub(r'\[\[Login to OpenAI ChatGPT\]\]\(\)\s*', '', response_content)
                    print(cleaned_content)
                    # Extract the answer number and explanation
                    match_q1 = re.search(r"\*\*Answer to Question 1:\*\*\s*(.+?)\s*(?:\*\*|$)", cleaned_content, re.DOTALL)
                    match_q2 = re.search(r"\*\*Answer to Question 2:\*\*\s*(.+?)\s*(?:\*\*|$)", cleaned_content, re.DOTALL)
                    #match_q1 = re.search(r"\*\*Answer to Question 1:\*\*\s*(\w+)", response_content, re.IGNORECASE)
                    #match_q2 = re.search(r"\*\*Answer to Question 2:\*\*\s*(\w+)", response_content, re.IGNORECASE)
                    match_explanation = re.search(r"\*\*Explanation:\*\*\s*(.*)", cleaned_content, re.DOTALL | re.IGNORECASE)
                    
                    fact_answer = match_q1.group(1) if match_q1 else None
                    llm_answer = match_q2.group(1) if match_q2 else None
                    llm_answer_explanation = match_explanation.group(1).strip() if match_explanation else None
                
                    llm_responses[id] = {
                        "fact_answer": fact_answer,
                        "llm_answer": llm_answer,
                        "llm_answer_explanation": llm_answer_explanation
                    } 

                    print(llm_responses[id])
                    # Add a small delay to avoid rate limiting
                    time.sleep(1)

                    print(f"record{counter} done")
                    counter += 1
                    
                except Exception as e:
                    continue

        if dataset_name == 'Code-Gen':
            ids = list(dataset.keys())
            for id in ids[:30]:  
                task = dataset[id]["task"]
                correct_code = dataset[id]["correct_code"] 
                correct_explanation = dataset[id]["correct_explanation"] 
                counter_explanation = dataset[id]["counter_explanation"] 

                prompt = str(get_prompt(dataset_name, mode)).format(
                    task = task.strip(),
                    correct_code = correct_code.strip(),
                    correct_explanation = correct_explanation.strip(),
                    counter_explanation = counter_explanation.strip()
                )

                try:
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                    )

                    response_content = response.choices[0].message.content.strip()
                    
                    # Remove the unwanted [[Login to OpenAI ChatGPT]]() part
                    cleaned_content = re.sub(r'\[\[Login to OpenAI ChatGPT\]\]\(\)\s*', '', response_content)
                    # print(cleaned_content)

                    # Extract the answer number and explanation
                    match_q = re.search(r"\*\*Answer to Question:\*\*\s*(.+?)\s*(?:\*\*|$)", cleaned_content, re.DOTALL)
                    match_explanation = re.search(r"\*\*Explanation:\*\*\s*(.*)", cleaned_content, re.DOTALL | re.IGNORECASE)
                    
                    llm_answer = match_q.group(1) if match_q else None
                    llm_answer_explanation = match_explanation.group(1).strip() if match_explanation else None
                
                    llm_responses[id] = {
                        "llm_answer": llm_answer,
                        "llm_answer_explanation": llm_answer_explanation
                    } 

                    print(llm_responses[id])
                    # Add a small delay to avoid rate limiting
                    time.sleep(1)

                    print(f"record{counter} done")
                    counter += 1
                    
                except Exception as e:
                    continue
        
        if dataset_name == 'Code-Sum':
            ids = list(dataset.keys())
            for id in ids[:30]:  
                task = dataset[id]["task"]
                correct_code = dataset[id]["correct_code"] 
                incorrect_code = dataset[id]["incorrect_code"] 
                correct_explanation = dataset[id]["correct_explanation"] 
    
                prompt = str(get_prompt(dataset_name, mode)).format(
                    task = task.strip(),
                    correct_code = correct_code.strip(),
                    incorrect_code = incorrect_code.strip(),
                    explanation = correct_explanation.strip()
                )
               
                try:
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                    )

                    response_content = response.choices[0].message.content.strip()
                    
                    # Remove the unwanted [[Login to OpenAI ChatGPT]]() part
                    cleaned_content = re.sub(r'\[\[Login to OpenAI ChatGPT\]\]\(\)\s*', '', response_content)
                    print(cleaned_content)

                    # Extract the answer number and explanation
                    # match_q = re.search(r"\*\*Answer to Question:\*\*\s*(.+?)\s*(?:\*\*|$)", cleaned_content, re.DOTALL)
                    match_q = re.search(r"(?:\*\*)?Counter Explanation:(?:\*\*)?\s*(.+?)(?:\s*(?=\*\*|$))", cleaned_content, re.DOTALL)
                    # match_explanation = re.search(r"\*\*Explanation:\*\*\s*(.*)", cleaned_content, re.DOTALL | re.IGNORECASE)
                    # match_explanation = re.search(r"(?:\*\*)?Explanation:(?:\*\*)?\s*(.*)", cleaned_content, re.DOTALL | re.IGNORECASE)

                    
                    llm_answer = match_q.group(1) if match_q else None
                    # llm_answer_explanation = match_explanation.group(1).strip() if match_explanation else None
                
                    llm_responses[id] = {
                        "llm_answer": llm_answer,
                        # "llm_answer_explanation": llm_answer_explanation
                    } 

                    print(llm_responses[id])
                    # Add a small delay to avoid rate limiting
                    time.sleep(1)

                    print(f"record{counter} done")
                    counter += 1
                    
                except Exception as e:
                    continue
        

        if dataset_name == 'MalAlgoQA':
            ids = list(dataset.keys())
            for id in ids[:10]:
                rationales = []  
                question = dataset[id]["question"]
                answer =  dataset[id]["answer"]
                choice_A = dataset[id]["choice_A"] 
                choice_B = dataset[id]["choice_B"]  
                choice_C = dataset[id]["choice_C"] 
                choice_D = dataset[id]["choice_D"] 
                rationale_A = dataset[id]["rationale_A"] 
                rationale_B = dataset[id]["rationale_B"]  
                rationale_C = dataset[id]["rationale_C"] 
                rationale_D = dataset[id]["rationale_D"] 
                if answer == 'A':
                    rationales = [rationale_B, rationale_C,rationale_D]
                elif answer == 'B':
                    rationales = [rationale_A, rationale_C,rationale_D]
                elif answer == 'C':
                    rationales = [rationale_A, rationale_B,rationale_D]
                elif answer == 'D':
                    rationales = [rationale_A, rationale_B,rationale_C]

                for rationale in rationales:
                    prompt = str(get_prompt(dataset_name, mode)).format(
                        question = question.strip(),
                        cr = rationale.strip(),
                        choice_A = choice_A,
                        choice_B = choice_B,
                        choice_C = choice_C,
                        choice_D = choice_D
                    )

                    try:
                        response = client.chat.completions.create(
                            model=model,
                            messages=[{"role": "user", "content": prompt}],
                        )

                        response_content = response.choices[0].message.content.strip()
                        
                        # Remove the unwanted [[Login to OpenAI ChatGPT]]() part
                        cleaned_content = re.sub(r'\[\[Login to OpenAI ChatGPT\]\]\(\)\s*', '', response_content)

                        # Extract the answer letter and explanation
                        match = re.search(r'^\s*([A-Za-z])\s*\n(.*)', cleaned_content, re.DOTALL)

                        if match:
                            llm_answer = match.group(1).strip()
                            llm_answer_explanation = match.group(2).strip()
                
                        llm_responses[rationale] = { 
                            "llm_answer": llm_answer, 
                            "llm_answer_explanation": llm_answer_explanation 
                        }
                        print(llm_responses[rationale])
                        # Add a small delay to avoid rate limiting
                        time.sleep(1)

                        print(f"record{counter} done")
                        counter += 1
                        
                    except Exception as e:
                        print(f"record{counter} done")
                        counter += 1
                        continue
            
        if dataset_name == "Syntax":
            keys = list(dataset.keys())
            for original_sentence in keys[:30]:
                prompt = str(get_prompt(dataset_name, mode)).format(
                    sentence = original_sentence
                )
                try:
                    #response = g4f.ChatCompletion.create(
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    response_content = response.choices[0].message.content.strip()
                    #response_content = response.strip()

                    # Remove the unwanted [[Login to OpenAI ChatGPT]]() part
                    cleaned_content = re.sub(r'\[\[Login to OpenAI ChatGPT\]\]\(\)\s*', '', response_content)
                    
                    # Match answers and explanations
                    match_answer = re.search(r"Answer to Question:\s*\*{0,2}\s*(.+)", cleaned_content)
                    match_explanation = re.search(r"Explanation:\s*\*{0,2}\s*(.+)", cleaned_content)
                    if match_answer:
                        llm_answer = match_answer.group(1).strip() if match_answer else None
                    if match_explanation:
                        llm_explanation = match_explanation.group(1).strip() if match_explanation else None
                    llm_responses[original_sentence] = { 
                        "llm_answer": llm_answer, 
                        "llm_explanation": llm_explanation 
                    }
                    print(llm_responses[original_sentence])
                    # Add a small delay to avoid rate limiting
                    time.sleep(1)
                    
                    print(f"record{counter} done")
                    counter += 1

                except Exception as e:
                    continue

        output_dir = f'./outputs/{mode}'
        os.makedirs(output_dir, exist_ok=True)
        
        with open(f'{output_dir}/{dataset_name}_{model}_llm_responses.json', 'w') as file:
            json.dump(llm_responses, file, indent=4)

def main(models, dataset_name):

    dataset = load_all_datasets(dataset_name)
    #print(dataset['HumanEval_0_test0'])
    print(f"{dataset_name}: There are {len(dataset)} records read from the input dataset")
    run_inference(models, dataset, mode)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run inference on specified models and dataset.")
    
    parser.add_argument(
        '--models', 
        type=str, 
        required=True,
        help="Comma-separated list of models to use. Example: gpt-4o,llama-3.1-70b"
    )
    
    parser.add_argument(
        '--dataset', 
        type=str, 
        required=True,
        help="Name of the dataset to load. Example: CRASS"
    )
    
    parser.add_argument(
        '--mode', 
        type=str, 
        required=True,
        help="Experiments mode. Example: zero_shot"
    )

    args = parser.parse_args()
    
    # Split the models string into a list
    models = args.models.split(',')
    dataset_name = args.dataset
    mode = args.mode
    main(models, dataset_name)


















'''
List of available models: ['gpt-4', 'gpt-4o', 'gpt-4o-mini', 'gemini-2.0-pro', 'gemini-2.0-flash', 'llama-3.1-405b', 'llama-3.1-70b', 'llama-3.1-8b', 'llama-3.2-90b', 'qwen-2-72b', 'deepseek-v3', 'claude-3.7-sonnet', 'claude-3-sonnet', 'blackboxai-pro', 'blackboxai']




                    # Match answers and explanations
                    # **Modified Argument: [answer]**
                    match_answer = re.search(r"\*\*Modified Argument:\s*(.*?)\*\*", cleaned_content, re.DOTALL | re.IGNORECASE)
                    if match_answer == None:
                        # **Modified Argument:**
                        # answer
                        match_answer = re.search(r"\*\*Modified Argument:\*\*\s*\n(.*?)(?=\n\s*\*\*Explanation:|\Z)", cleaned_content, re.DOTALL | re.IGNORECASE)
                    if match_answer == None:
                        match_answer = re.search(r"\*\*Modified Argument:\*\*\s*(\w+)", response_content, re.IGNORECASE)
                    match_explanation = re.search(r"\*\*Explanation:\s*(.*?)\*\*", cleaned_content, re.DOTALL | re.IGNORECASE)
                    if match_explanation == None:
                        match_explanation = re.search(r"\*\*Explanation:\*\*\s*\n(.*)", cleaned_content, re.DOTALL | re.IGNORECASE)
                    if match_explanation == None:
                        match_explanation = re.search(r"\*\*Explanation:\n\*\*\s*(\w+)", cleaned_content, re.DOTALL | re.IGNORECASE)
                    
                    # match_answer = re.search(r"\*\*Modified Argument:\*\*\s*(.*)", cleaned_content, re.DOTALL | re.IGNORECASE)
                    # match_answer = re.search(r"\*\*Modified Argument:\*\*\s*(.*?)(?=\n\s*\*\*Explanation:|\Z)", cleaned_content, re.DOTALL | re.IGNORECASE)
                    
'''