'''
def get_prompt_decomp(dataset_name, mode):
    if (dataset_name == 'CRASS' and mode == 'zero_shot'):
        return '''
''' 
        # Role: Counterfactual Reasoning Analyst  
        Your task is to identify causal variables and generate "factual_edges" and "counterfactual_edges". All outputs must follow strict JSON formatting for automated saving.  

        ## Context Format  
        **Premise:**  
        {premise}  

        **Questionized Counterfactual Conditional (QCC):**  
        {qcc}  

        ## Task Instructions  
        1. **Variable Identification**  
        - Extract and classify variables into:  
            - `Exposure (X)`: Direct intervention (verb phrase, e.g., "act of opening").  
            - `Outcome (Y)`: Final result (state phrase, e.g., "chest opened").  
            - `Covariate (Z)`: Pre-existing conditions influencing X/Y (≥2 noun phrases).  
            - `Mediator (M)`: Mechanism linking X→Y (physical/logical process).  

        2. **Causal Graph Construction**  
        - Build factual/counterfactual edges using variable relationships.  
        
        ## Output Format  
        ```json
        {
            "factual_roles": {
                "Exposure": ["X_value"],
                "Covariate": ["Z1", "Z2"],
                "Mediator": ["M_value"],
                "Outcome": ["Y_value"]
            },
            "counterfactual_roles": {
                "Exposure": ["X'_value"],
                "Covariate": ["Z1", "Z2"],
                "Mediator": ["M'_value"],
                "Outcome": ["Y'_value"]
            },
            "causal_graph": {
                "factual_edges": [["Z1→X"], ["X→M"], ["M→Y"], ...],
                "counterfactual_edges": [["Z1→X'"], ["X'→M'"], ["M'→Y'"], ...]
            }
        }
        ```
        [Your Response]
'''   
def get_prompt(dataset_name, mode):
    if (dataset_name == 'CRASS' and mode == 'zero_shot'):
        return '''
        ### Context:
        Below is a base Premise Explication and a Questionized Counterfactual Conditional(QCC).

        **Premise:**
        {premise}

        **Questionized Counterfactual Conditional(QCC):**
        {qcc} 

        ### Task:
        which answer is most suitable in the presented hypothetical situation?

        ### Answers:
        1 {answer1}
        2 {answer2}
        3 {answer3}
        4 {answer4}
        Please provide the answer number (1, 2, 3, or 4) in a line. The answer should just a plain number without any formatting and not followed by anything.
        And please provide a brief explanation in a new line. 

        ### Requirements:
        - Provide a clear and concise answer.
        - Ensure accuracy and relevance to the Premise and QCC.

        [Your Response]
        '''
    if (dataset_name == 'CRASS' and mode == 'few_shots'):
        return '''
       ### Context:
        Below is a base Premise Explication and a Questionized Counterfactual Conditional (QCC). 

        **Premise:**  
        {premise}

        **Questionized Counterfactual Conditional (QCC):**  
        {qcc} 

        ### Task:  
        Which answer is most suitable in the presented hypothetical situation?  

        ### Answers:
        1 {answer1}
        2 {answer2}
        3 {answer3}
        4 {answer4}
        Please provide the answer number (1, 2, 3, or 4) in a line. The answer should just a plain number without any formatting and not followed by anything.
        And please provide a brief explanation in a new line. 

        ### Requirements:  
        - Use the below provided examples as references.  
        - Provide a clear and concise answer.  
        - Ensure accuracy and relevance to the Premise and QCC. 

        ### Few-Shot Examples:
        #### Example 1:
        # **Premise:**  
        # A woman opens a treasure chest.  

        # **QCC:**  
        # What would have happened if the woman had not opened the treasure chest?  

        # **Answers:**  
        # 1. The treasure chest would have been open.  
        # 2. That is not possible.  
        # 3. The treasure chest would have remained closed. ✅  
        # 4. I don't know.  

        # **Correct Answer:**  
        # 3  

        # **Explanation:**  
        # If the woman had not opened the treasure chest, it would have remained closed, as no other action is stated that would have caused it to open.

        # #### Example 2:
        # **Premise:**  
        # A police officer calms down a hostage taker.  

        # **QCC:**  
        # What would have happened if the police officer had not calmed the hostage taker?  

        # **Answers:**  
        # 1. That is not possible.  
        # 2. The hostages would have remained in danger. ✅  
        # 3. The hostage taker would have been shot.  
        # 4. The hostage taker would have released the hostages anyway.  

        # **Correct Answer:**  
        # 2  

        # **Explanation:**  
        # If the police officer had not calmed the hostage taker, the hostages would have remained in danger since no de-escalation occurred.

        # #### Example 3:
        # **Premise:**  
        # A man talks about a lion.  

        # **QCC:**  
        # What would have happened if the man had talked to the lion?  

        # **Answers:**  
        # 1. Without a barrier, the man would have been eaten. ✅  
        # 2. Without a barrier, the lion would have been eaten.  
        # 3. Nothing special would have happened.  
        # 4. Without a barrier, they would have had a nice conversation.  

        # **Correct Answer:**  
        # 1  

        # **Explanation:**  
        # If the man had talked to the lion without a barrier, he would have been eaten, as lions are dangerous predators.

        # #### Example 4:
        # **Premise:**  
        # A girl kisses a boy.  

        # **QCC:**  
        # What would have happened if the girl had slapped the boy?  

        # **Answers:**  
        # 1. The girl would have been angry. ✅  
        # 2. The girl would have been happy.  
        # 3. That is not possible.  
        # 4. Everything would have been fine.  

        # **Correct Answer:**  
        # 1  

        # **Explanation:**  
        # If the girl had slapped the boy instead of kissing him, it would likely indicate that she was angry.

        # #### Example 5:
        # **Premise:**  
        # A girl kisses a boy.  

        # **QCC:**  
        # What would have happened if the girl had killed the boy?  

        # **Answers:**  
        # 1. That is not possible.  
        # 2. She would have been liable to prosecution. ✅  
        # 3. The boy would have been arrested for assault.  
        # 4. The boy would have kissed the girl.  

        # **Correct Answer:**  
        # 2  

        # **Explanation:**  
        # If the girl had killed the boy, she would have been liable to prosecution as killing is a crime.

        # [Your Response]

        '''
    if (dataset_name == 'CRASS' and mode == 'CoT'):
        return '''
        ### Context:
        Below is a base Premise Explication and a Questionized Counterfactual Conditional(QCC).

        **Premise:**
        {premise}

        **Questionized Counterfactual Conditional(QCC):**
        {qcc} 

        ### Task:
        which answer is most suitable in the presented hypothetical situation?

        ### Answers:
        1 {answer1}
        2 {answer2}
        3 {answer3}
        4 {answer4}
        Please first think through the question step-by-step, considering the logical implications of the Premise and QCC.
        After your reasoning, please provide the answer number (1, 2, 3, or 4) in a single line. The answer should just a plain number without any formatting and not followed by anything.
        Then, on a new line, briefly explain your final choice.

        ### Requirements:
        - Think step-by-step before answering.
        - Provide a clear and concise answer.
        - Ensure accuracy and relevance to the Premise and QCC.

        [Your Response]
        '''
    if  (dataset_name == 'CVQA-Boolean' and mode == 'zero_shot'):
        return """
        ### Task: 
        Analyze the provided image {image_path} and answer the following two questions based on its content. 
        -  Quesiton 1: {fact_query}
        -  Question 2: {counter_query}
        Please respond the first question strictly with 'yes' or 'no' on one line starting with **Answer to Question 1:**". 
        Please respond the second question strictly with 'yes' or 'no' on one line starting with **Answer to Question 2:**".
        
        ### Response Format:
        Answer the first question strictly with either 'yes' or 'no' on a single line, formatted as:
        Answer to Question 1: [yes/no]
        Answer the second question strictly with either 'yes' or 'no' on a single line, formatted as:
        Answer to Question 2: [yes/no]
        Provide a brief explanation for your answer to Question 2 on a new line, formatted as:
        Explanation: [your reasoning]

        ### Important Guidelines:
        - **Base your reasoning on the provided image.**
        - **Do not** include any additional text or interpretations beyond the required answers and explanation.

        """
    if  (dataset_name == 'CVQA-Boolean' and mode == 'few_shots'):
        return """
        ### Task: 
        Analyze the provided image {image_path} and answer the following two questions based on the reasoning on the provided image. 
        -  Quesiton 1: {fact_query}
        -  Question 2: {counter_query}
        Please respond the first question strictly with 'yes' or 'no' on one line starting with **Answer to Question 1:**". 
        Please respond the second question strictly with 'yes' or 'no' on one line starting with **Answer to Question 2:**".
        
        ### Response Format:
        Answer the first question strictly with either 'yes' or 'no' on a single line, formatted as:
        **Answer to Question 1:** [yes/no]
        Answer the second question strictly with either 'yes' or 'no' on a single line, formatted as:
        **Answer to Question 2:** [yes/no]
        Provide a brief explanation for your answer to Question 2 on a new line, formatted as:
        **Explanation:** [your reasoning]

        ### Important Guidelines:
        - Use the below provided **Few-Shot Examples** as references. 
        - **Base your reasoning on the provided image.**
        - **Do not** include any additional text or interpretations beyond the required answers and explanation.

        ### Few-Shot Examples:
        #### Example 1:
        **Task:**  
        Analyze the provided image COCO_val2014_000000000042.jpg and answer the following two questions based on the reasoning on the provided image.
        -  Quesiton 1: Is there a red sandal here?
        -  Question 2: Would there be a red sandal here if all shoes were removed?

        **Correct Answer to Question 1:**  
        **Answer to Question 1:** yes

        **Correct Answer to Question 2:**  
        **Answer to Question 2:** no 

        **Explanation:**  
        **Explanation:** Because red sandal is a kind of shoes, if all shoes were removed, the red sandal was also removed. 

        #### Example 2:
        **Task:**  
        Analyze the provided image COCO_val2014_000000000873.jpg and answer the following two questions based on the reasoning on the provided image.
        -  Quesiton 1: Is this a hospital??
        -  Question 2: Would this be a hospital if there were red crosses on the roof?
        
        **Correct Answer to Question 1:**  
        **Answer to Question 1:** no

        **Correct Answer to Question 2:**  
        **Answer to Question 2:** yes 

        **Explanation:** The presence of red crosses on the roof would be a strong visual indicator that the building is a hospital, as red crosses are commonly associated with medical facilities and emergency services.
         
        #### Example 3:
        **Task:**  
        Analyze the provided image COCO_val2014_000000000164.jpg and answer the following two questions based on the reasoning on the provided image.
        -  Quesiton 1: Is this a hospital??
        -  Question 2: How many paper towel rolls would be seen if the plates were removed?
        
        **Correct Answer to Question 1:**  
        **Answer to Question 1:** no

        **Correct Answer to Question 2:**  
        **Answer to Question 2:** 1 

        **Explanation:** The presence of red crosses on the
    
    
    "COCO_val2014_000000000164.jpg": {
        "query": "How many paper towel rolls would be seen if the plates were removed?",
        "answer": "1"
    },
    "COCO_val2014_000000000143.jpg": {
        "query": "How many birds would still be in the tree if a hunter fired a shot at a bird?",
        "answer": "0"
    },
    "COCO_val2014_000000000074.jpg": {
        "query": "Would this dog have a collar if the dog had a rope around its neck?",
        "answer": "no"
    },

        """
    if  (dataset_name == 'CVQA-Boolean' and mode == 'CoT'):
        return """
        ### Task: 
        Analyze the provided image {image_path} and answer the following two questions based on its content. 
        -  Quesiton 1: {fact_query}
        -  Question 2: {counter_query}
        Please first think through the question step-by-step. 
        After your reasoning, please respond the first question strictly with 'yes' or 'no' on one line starting with **Answer to Question 1:**". 
        And please respond the second question strictly with 'yes' or 'no' on one line starting with **Answer to Question 2:**".
        And provide a brief explanation for your answer to Question 2 on a new line starting with **Explanation:**". 

        ### Important Guidelines:
        - **Base your reasoning on the provided image.**
        - **Think step-by-step before answering.**
        - **Do not** include any additional text or interpretations beyond the required answers and explanation.

        """
    if  (dataset_name == 'CVQA-Numerical' and mode == 'CoT'):
        return """
        ### Task: 
        Analyze the provided image {image_path} and answer the following two questions based on its content.
        - Question 1: {fact_query}
        - Question 2: {counter_query}
        Please first think through the question step-by-step. 
        After your reasoning, please respond the first question strictly with a single number on one line starting with **Answer to Question 1:**". 
        And please respond the second question strictly with a single number on one line starting with **Answer to Question 2:**".
        And provide a brief explanation for your answer to Question 2 on a new line starting with **Explanation:**". 

        ### Important Requirements:
        - **Base your reasoning on the provided image.**
        - **Think step-by-step before answering.**
        - **Do not** include any additional text or interpretations beyond the required answers and explanation.

        """
    if  (dataset_name == 'CVQA-Numerical' and mode == 'zero_shot') or (dataset_name == 'CVQA--Numerical-Direct' and mode == 'zero_shot') or (dataset_name == 'CVQA--Numerical-Indirect' and mode == 'zero_shot') :
        return """
        ### Task: 
        Analyze the provided image {image_path} and answer the following two questions based on its content.
        - Question 1: {fact_query}
        - Question 2: {counter_query}

        ### Response Format:
        Answer the first question strictly with a single number on one line, formatted as:
        Answer to Question 1: [number]
        Answer the second question strictly with a single number on one line, formatted as:
        Answer to Question 2: [number]
        Provide a brief explanation for your answer to Question 2 on a new line, formatted as:
        Explanation: [your reasoning]

        ### Important Guidelines:
        - **Base your reasoning on both the images and their captions.**  
        - **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.    
        """
    if  (dataset_name == 'COCO' and mode == 'zero_shot'):
        return"""
        ### Context:
        Below are two images, each accompanied by a descriptive caption. One caption is a counterfactual variation of the other. The two captions are identical to each other except a noun subject. 

        **Premise:**
        The following image {fact_image} illustrates the situation described by a caption that **{fact_caption}**.

        **Counterfactual Condition (CC):**
        The counterfactual caption is **{counter_caption}**, which is identical to the other caption except a noun subject. 

        ### Task:
        Your task is to determine whether the new image **{counter_image}** represents the **Counterfactual Condition (CC)** described above.  
        To evaluate this, compare the new image against the counterfactual caption and assess if it aligns with the intended change from the premise.
        
        ### Response Format:
        Strictly follow the response format below:  
        - Answer with **either** 'yes' or 'no' **on a single line**, formatted as:
        **Answer to Question: [yes/no]**  
        - Provide a **brief** explanation supporting your answer **on a new line**, formatted as:
        **Explanation: [your reasoning]**  

        ### Important Guidelines:
        - **Base your reasoning on both the images and their captions.**  
        - **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.    
        """
    if  (dataset_name == 'COCO' and mode == 'CoT'):
        return"""
        ### Context:
        Below are two images, each accompanied by a descriptive caption. One caption is a counterfactual variation of the other. The two captions are identical to each other except a noun subject. 

        **Premise:**
        The following image {fact_image} illustrates the situation described by a caption that **{fact_caption}**.

        **Counterfactual Condition (CC):**
        The counterfactual caption is **{counter_caption}**, which is identical to the other caption except a noun subject. 

        ### Task:
        Your task is to determine whether the new image **{counter_image}** contains the changed noun subject described in the **Counterfactual Condition (CC)**.  
        
        Let's think step by step:

        1. Identify the noun subject difference between the premise caption and the counterfactual caption.
        2. Analyze the content of the new image {counter_image} to see if it aligns with the noun subject in the counterfactual caption.
        3. Determine whether the new image contains the noun subject that is described by the counterfactual caption which is different from the premise caption.
        
        ### Response Format:
        After your reasoning, **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        Strictly follow the response format below:  
        - Answer with **either** 'yes' or 'no' **on a single line**, formatted as:
        **Answer to Question: [yes/no]**  
        - Provide a **brief** explanation supporting your answer **on a new line**, formatted as:
        **Explanation: [your reasoning]**  

        ### Important Guidelines:
        - **Base your reasoning on both the images and their captions.**     
        """
    if  (dataset_name == 'Arithmetic-Base-8' and mode == 'zero_shot'):
        return"""
        You are a mathematician. Assuming that all numbers are in base-8 where the digits are "01234567", what is {num1}+{num2}? 
        Response Format:
        - Provide your answer **on a single line**, formatted as:. 
        **Answer to Question: [your answer]**
        - Provide a **brief** explanation supporting your answer **on a new line**, formatted as:
        **Explanation: [your reasoning]**
        """
    if  (dataset_name == 'Arithmetic-Base-9' and mode == 'zero_shot'):
        return"""
        You are a mathematician. Assuming that all numbers are in base-9 where the digits are "012345678", what is {num1}+{num2}? 
        Response Format:
        - Provide your answer **on a single line**, formatted as:. 
        **Answer to Question: [your answer]**
        - Provide a **brief** explanation supporting your answer **on a new line**, formatted as:
        **Explanation: [your reasoning]**
        """
    if  (dataset_name == 'Arithmetic-Base-9' and mode == 'CoT'):
        return"""
        You are a mathematician. Assuming that all numbers are in base-9 where the digits are "012345678", what is {num1}+{num2}? 
        Please first think through the question step-by-step, considering converting both numbers from base-9 to base-10. Then, adding the two base-10 numbers. Finally, converting the result back to base-9.
        After your reasoning, please response just the final answer without showing the chain of thoughts.
        Response Format:
        - **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        - Provide your answer **on a single line**, formatted as:. 
        **Answer to Question: [your answer]**
        - Provide a **brief** explanation supporting your answer **on a new line**, formatted as:
        **Explanation: [your reasoning]**
        """
    if  (dataset_name == 'Arithmetic-Base-11' and mode == 'zero_shot'):
        return"""
        You are a mathematician. Assuming that all numbers are in base-11 where the digits are "0123456789A", what is {num1}+{num2}? 
        Response Format:
        - Provide your answer **on a single line**, formatted as:. 
        **Answer to Question: [[your answer]**
        - Provide a **brief** explanation supporting your answer **on a new line**, formatted as:
        **Explanation: [your reasoning]**
        """
    if  (dataset_name == 'Arithmetic-Base-16' and mode == 'zero_shot'):
        return """
        You are a mathematician. Assuming that all numbers are in base-16 where the digits are "0123456789ABCDEF", what is {num1}+{num2}? 
        Response Format:
        Provide your answer **on a single line**, formatted as:. 
        **Answer to Question: [your answer]**
        - Provide a **brief** explanation supporting your answer **on a new line**, formatted as:
        **Explanation: [your reasoning]**
        """
    if  (dataset_name == 'Arithmetic-Base-16' and mode == 'CoT'):
        return"""
        You are a mathematician. Assuming that all numbers are in base-16 where the digits are "0123456789ABCDEF", what is {num1}+{num2}? 
        Please first think through the question step-by-step, considering converting both numbers from base-16 to base-10. Then, adding the two base-10 numbers. Finally, converting the result back to base-16.
        After your reasoning, please response just the final answer without showing the chain of thoughts.
        Response Format:
        - **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        - Provide your answer **on a single line**, formatted as:. 
        **Answer to Question: [your answer]**
        - Provide a **brief** explanation supporting your answer **on a new line**, formatted as:
        **Explanation: [your reasoning]**
        """
    if (dataset_name == 'CLOMO' and mode == 'zero_shot'):
        return '''
        ### Context: 
        {instruction}

        **Argument:**
        {argument}

        **Premise1:**
        {premise1}

        **Premise2:**
        {premise2}

        ### Task:
        {task}
        Please write the Modified Argument on one line strictly starting with **Modified Argument:**". **Do not** repeat Premise1 and Premise2. 
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        And provide a **brief** explanation supporting your answer on another line strictly starting with **Explanation:**. 
        '''
    if (dataset_name == 'CLOMO' and mode == 'CoT'):
        return '''
        ### Context: 
        {instruction}

        **Argument:**
        {argument}

        **Premise1:**
        {premise1}

        **Premise2:**
        {premise2}

        ### Task:
        {task}
        Please first think through the question step-by-step, considering how Premise1 and Premise2 interact with the Argument. Then determine the necessary modifications to the Argument so that Premise2 meet the requirement of the task, while Premise1 does not. Ensure that no additional statements are added beyond the original Argument.
        After your reasoning, please write the Modified Argument on one line strictly starting with **Modified Argument:**". **Do not** repeat Premise1 and Premise2. 
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        And provide a **brief** explanation supporting your answer on another line strictly starting with **Explanation:**.
        '''
    if (dataset_name == 'Code-Exe' and mode == 'zero_shot'):
        return '''
        ### Context:
        You are an expert programmer. You are given the following instruction of a function and an input of a test case.
        
        **Instruction:**
        {instruction}

        **Input:**
        {input}
        
        ### Task:
        There are two questions.
        - Quesiton 1: What is the output of the input test case based the default indexing of Python?
        - Quesiton 2: We assume a conterfacutal condition that the indexing is 1-based *NOT" 0-based, then what is the output of the test case in 1-based indexing?
        Please respond the first question on one line strictly starting with **Answer to Question 1:**". 
        Please respond the second question on another line strictly starting with **Answer to Question 2:**".
        In addition, Provide a **brief** explanation for the answer to question 2 on another line strictly starting with **Explanation:**".
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        '''
    if (dataset_name == 'Code-Exe' and mode == 'CoT'):
        return '''
        ### Context:
        You are an expert programmer. You are given the following instruction of a function and an input of a test case.
        
        **Instruction:**
        {instruction}

        **Input:**
        {input}
        
        ### Task:
        There are two questions.
        - Quesiton 1: What is the output of the input test case based the default indexing of Python?
        - Quesiton 2: We assume a conterfacutal condition that the indexing is 1-based *NOT" 0-based, then what is the output of the test case in 1-based indexing?
        Please first think through the question step-by-step, considering the conterfactual condition. 
        After your reasoning, please response just the final answer without showing the chain of thoughts.
        Please respond the first question on one line strictly starting with **Answer to Question 1:**". 
        Please respond the second question on another line strictly starting with **Answer to Question 2:**".
        In addition, Provide a **brief** explanation for the answer to question 2 on another line strictly starting with **Explanation:**".
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked
        '''
    if (dataset_name == 'Code-Gen' and mode == 'zero_shot'):
        return '''
        ### Context: 
        You are an AI-Coding assistant. In the following, you will see a task, a piece of correct code that was accepted by the task, and two explanations, where the correct explanation provides an explanation to the correct code and the counter explanation provides an explanation to the incorrect code which is similar to the correct code but is incorrect.   

        **Task:**
        {task}

        **Correct Code:**
        {correct_code}

        **Correct Explanation:**
        {correct_explanation}

        **Counter Explanation:**
        {counter_explanation}

        ### Task:
         Your goal is to generate the flawed code that has the bugs described in the **Counter Explanation** 
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        Please give your answer on one line strictly starting with **Answer to Question:**". 
        In addition, provide a **brief** explanation of the answer on another line strictly starting with **Explanation:**".
        '''
    if (dataset_name == 'Code-Gen' and mode == 'CoT'):
        return '''
        ### Context: 
        You are an AI-Coding assistant. In the following, you will see a task, a piece of correct code that was accepted by the task, and two explanations, where the correct explanation provides an explanation to the correct code and the counter explanation provides an explanation to the incorrect code which is similar to the correct code but is incorrect.   

        **Task:**
        {task}

        **Correct Code:**
        {correct_code}

        **Correct Explanation:**
        {correct_explanation}

        **Counter Explanation:**
        {counter_explanation}

        ### Task:
        Your goal is to generate the flawed code that has the bugs described in the **Counter Explanation**
        Please first think through the question step-by-step, considering the counter_explanation. 
        After your reasoning, please response just the final answer without showing the chain of thoughts. 
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        Please give your answer on one line strictly starting with **Answer to Question:**". 
        In addition, provide a **brief** explanation of the answer on another line strictly starting with **Explanation:**".
        '''
    if (dataset_name == 'Code-Sum' and mode == 'zero_shot'):
        return '''
        ### Context: 
        You are an AI-Coding assistant. In the following, you will see a task, a piece of correct code that was accepted by the task, a piece of incorrect code that was rejected by the task, and an explanations which explains the correct code.

        **Task:**
        {task}

        **Correct Code:**
        {correct_code}

        **Incorrect Code:**
        {incorrect_code}

        **Explanation to the Correct Code:**
        {explanation}

        ### Task:
        Your goal is to address the issues and bugs of the input incorrect code in details. 
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        Please give your answer on one line strictly starting with **Answer to Question:**". 
        '''
    if (dataset_name == 'Code-Sum' and mode == 'CoT'):
        return '''
        ### Context: 
        You are an AI-Coding assistant. In the following, you will see a task, a piece of correct code that was accepted by the task, a piece of incorrect code that was rejected by the task, and an explanations which explainsn the correct code.

        **Task:**
        {task}

        **Correct Code:**
        {correct_code}

        **Incorrect Code:**
        {incorrect_code}

        **Explanation to the Correct Code:**
        {explanation}

        ### Task:
        Your goal is to address the issues and bugs of the input incorrect code in details after reading the incorrect code, correct code and explanation.. 
        Please first think through the question step-by-step after reading the incorrect code, correct code and explanation.
        After your reasoning, please response just the final answer without showing the chain of thoughts. 
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        Please give your answer on one line strictly starting with **Counter Explanation:**". 
        '''
    if (dataset_name == 'Code-Sum' and mode == 'few_shots'):
        return '''
        ### Context: 
        You are an AI-Coding assistant. In the following, you will see a task, a piece of correct code that was accepted by the task, a piece of incorrect code that was rejected by the task, and an explanations which explainsn the correct code.

        **Task:**
        {task}

        **Correct Code:**
        {correct_code}

        **Incorrect Code:**
        {incorrect_code}

        **Explanation to the Correct Code:**
        {explanation}

        ### Task:
        Your goal is to address the issues and bugs of the input incorrect code in details after reading the incorrect code, correct code and explanation. 
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        Please give your answer on one line strictly starting with **Answer to Question:**". 
        '''
    if (dataset_name == 'MalAlgoQA' and mode == 'zero_shot'):
        return '''
        ### Context:
        Below is a base Question and a Counterfactual Rationale(CR).

        **Question:**
        {question}

        **Counterfactual Rationale(CR):**
        {cr} 

        ### Task:
        which choice is most suitable to the base **Question** according to the **Counterfactual Rationale(CR)**?

        ### Answers:
        A {choice_A}
        B {choice_B}
        C {choice_C}
        D {choice_D}
        Please provide the answer (A, B, C, or D) on a line. The answer should just a plain single letter without any formatting and not followed by anything.
        And please provide a brief explanation of your answer on a new line. 
        

        ### Requirements:
        - Provide a clear and concise answer.
        - Ensure accuracy and relevance to the base **Question and the **Counterfactual Rationale(CR):**.

        [Your Response]
        '''
    if (dataset_name == 'MalAlgoQA' and mode == 'CoT'):
        return '''
        ### Context:
        Below is a base Question and a Counterfactual Rationale(CR).

        **Question:**
        {question}

        **Counterfactual Rationale(CR):**
        {cr} 

        ### Task:
        which choice is most suitable to the base **Question** according to the **Counterfactual Rationale(CR)**?

        ### Answers:
        A {choice_A}
        B {choice_B}
        C {choice_C}
        D {choice_D}

        Please first think through the task step-by-step after reading the question and the counterfactual rationale.
        After your reasoning, please provide the final answer (A, B, C, or D) on a line without showing the chain of thoughts.The answer should just a plain single letter without any formatting and not followed by anything.
        And please provide a brief explanation of your answer on a new line. 
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.

        [Your Response]
        '''
    if (dataset_name == 'MalAlgoQA' and mode == 'few_shots'):
        return '''
        ### Context:
        Below is a base Question and a Counterfactual Rationale(CR).

        ### Examples:

        **Question:**
        What was the mistake made in this solution?

        **Counterfactual Rationale(CR):**
        Did not use the conversion factor with the 2 dimensions. Calculated the volume in cubic feet, then divided by 62.43.

        **Answer:** B  
        **Explanation:** The rationale describes a volume error and unit issue, aligning with choice B.

        ---

        **Question:**
        What error occurred in the calculation?

        **Counterfactual Rationale(CR):**
        Multiplied all of the numbers provided.

        **Answer:** D  
        **Explanation:** The rationale suggests an overgeneralized multiplication, which matches D.

        ---

        **Question:**
        What inequality sign mistake was made?

        **Counterfactual Rationale(CR):**
        Used the incorrect inequality sign.

        **Answer:** B  
        **Explanation:** The rationale directly states the inequality sign was wrong, matching B.

        ---

        **Question:**
        How did the student incorrectly calculate the value?

        **Counterfactual Rationale(CR):**
        Calculated 2/3 of the incorrect value.

        **Answer:** C  
        **Explanation:** This describes a fractional operation on an incorrect base value, indicating C.

        ---

        **Question:**
        What conceptual and interpretation error occurred?

        **Counterfactual Rationale(CR):**
        Calculated 2/3 of the incorrect value and misinterpreted "at least."

        **Answer:** D  
        **Explanation:** This combines a computation and logical interpretation error, which D captures.

        ---

        ### Now Try This:

        **Question:**
        {question}

        **Counterfactual Rationale(CR):**
        {cr} 

        ### Task:
        which choice is most suitable to the base **Question** according to the **Counterfactual Rationale(CR)**?

        ### Answers:
        A {choice_A}
        B {choice_B}
        C {choice_C}
        D {choice_D}
        Please provide the answer (A, B, C, or D) on a line. The answer should just a plain single letter without any formatting and not followed by anything.
        And please provide a brief explanation of your answer on a new line. 
        

        ### Requirements:
        - Provide a clear and concise answer.
        - Ensure accuracy and relevance to the base **Question and the **Counterfactual Rationale(CR):**.

        [Your Response]
        '''
    if (dataset_name == 'Syntax' and mode == 'zero_shot'):
        return '''
        ### Context:
        You are an expert in linguistics. Imagine a new language that is the same as English only except that it uses the subject-object-verb order instead of the subject-verb-object order.
        You are given the following **Original Sentence**.
        
        **Original Sentence:**
        {sentence}

        ### Task:
        Your task is to reconstruct the original sentence in new language. You should **only** use the words in the **same** form as they appear in the given sentence. Ensure that no additional words are added beyond the words used in the **Original Sentence**.
        Please give your answer on one line strictly starting with **Answer to Question:**". 
        And provide a **brief** explanation for the answer on another line strictly starting with **Explanation:**".
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        '''
    if (dataset_name == 'Syntax' and mode == 'CoT'):
        return '''
        ### Context:
        You are an expert in linguistics. Imagine a new language that is the same as English only except that it uses the subject-object-verb order instead of the subject-verb-object order.
        You are given the following **Original Sentence**.
        
        **Original Sentence:**
        {sentence}

        ### Task:
        Your task is to reconstruct the original sentence in new language. You should **only** use the words in the **same** form as they appear in the given sentence. Ensure that no additional words are added beyond the words used in the **Original Sentence**.
        Please first think through the task step-by-step.
        After your reasoning, please give your answer on one line strictly starting with **Answer to Question:**". 
        And provide a **brief** explanation for the answer on another line strictly starting with **Explanation:**".
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        '''
    if (dataset_name == 'Syntax' and mode == 'few_shots'):
        return '''
        ### Context:
        You are an expert in linguistics. Imagine a new language that is the same as English only except that it uses the subject-object-verb order instead of the subject-verb-object order.
        You are given the following **Original Sentence**.

        ### Examples:
        **Original Sentence:**
        alice sees emma.

        **Answer to Question:** alice emma sees.
        **Explanation:** "alice" is the subject, "emma" is the object, and "sees" is the verb placed at the end.

        **Original Sentence:**
        tom calls emma.

        **Answer to Question:** tom emma calls.
        **Explanation:** "tom" is the subject, "emma" is the object, and "calls" is the verb placed at the end.

        **Original Sentence:**
        anna loves emily.

        **Answer to Question:** anna emily loves.
        **Explanation:** "anna" is the subject, "emily" is the object, and "loves" is the verb placed at the end.

        **Original Sentence:**
        tom saw jacob.

        **Answer to Question:** tom jacob saw.
        **Explanation:** "tom" is the subject, "jacob" is the object, and "saw" is the verb placed at the end.

        **Original Sentence:**
        tim knows jacob.

        **Answer to Question:** tim jacob knows.
        **Explanation:** "tim" is the subject, "jacob" is the object, and "knows" is the verb placed at the end.

        ### Task:
        Now, apply the same logic to the next sentence.

        **Original Sentence:**
        {sentence}

        Your task is to reconstruct the original sentence in new language. You should **only** use the words in the **same** form as they appear in the given sentence. Ensure that no additional words are added beyond the words used in the **Original Sentence**.
        
        Please give your answer on one line strictly starting with **Answer to Question:**". 
        And provide a **brief** explanation for the answer on another line strictly starting with **Explanation:**".
        **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.
        '''










































    '''

    Your task is to determine whether the new image **{counter_image}** represents the **Counterfactual Condition (CC)** described above.  



    
    You are a mathematician. Assuming that all numbers are in base-8 where the digits are "01234567", what is {8_num1}+{8_num2}? The response with the result in **Answer to Question 2:**
    You are a mathematician. Assuming that all numbers are in base-9 where the digits are "012345678", what is {9_num1}+{9_num2}? The response with the result in **Answer to Question 3:**
    You are a mathematician. Assuming that all numbers are in base-11 where the digits are "0123456789A", what is {11_num1}+{11_num2}? The response with the result in **Answer to Question 4:**
    You are a mathematician. Assuming that all numbers are in base-16 where the digits are "0123456789ABCDEF", what is {16_num1}+{16_num2}? The response with the result in **Answer to Question 5:**
    
    Task: Read the provided image {image_path} and answer two questions.
        -  Quesiton 1: {fact_query}
        -  Question 2: {counter_query}
        Please respond for the first question strictly with one number on one line starting with **Answer to Question 1:**". 
        Please respond for the second question strictly with one number on one line starting with **Answer to Question 2:**".
        For the second question, please provide a brief explanation on another line starting with **Explanation:**. 
        
     
     Task: 
        Analyze the provided image {image_path} and answer the following two questions based on its content.
        - Question 1: {fact_query}
        - Question 2: {counter_query}

        Response Format:
        Answer the first question strictly with a single number on one line, formatted as:
        Answer to Question 1: [number]
        Answer the second question strictly with a single number on one line, formatted as:
        Answer to Question 2: [number]
        Provide a brief explanation for your answer to Question 2 on a new line, formatted as:
        Explanation: [your reasoning]

        Important: Do not include any additional text, units, or interpretations beyond the required number responses and explanation.

        Below is a base Premise Explication with an image and a Counterfactual Condition(CC) with an image.

        **Premise:**
        The below image {fact_image} describes the condition of {fact_caption}

        **Counterfactual Condition(CC):**
        The counterfactual condition is {counter_caption}

        ### Task:
        Whether the new image {counter_image} addresses the above Conterfactual Condition(CC)? 

        ### Response Format:
        Answer the question strictly with either 'yes' or 'no' on a single line, formatted as:
        Answer to Question: [yes/no]
        Provide a brief explanation for your answer to the question on a new line, formatted as:
        Explanation: [your reasoning]

        Important: Do not include any additional text, units, or interpretations beyond the required number responses and explanation.
    
    return 
        ### Context:
        Below is a **Premise Explication** with an image and a **Counterfactual Condition (CC)**, each accompanied by a descriptive caption.

        **Premise:**
        The following image {fact_image} illustrates the situation described by **{fact_caption}**.

        **Counterfactual Condition (CC):**
        The expected counterfactual scenario is **{counter_caption}**.

        ### Task:
        Your task is to determine whether the new image **{counter_image}** accurately represents the **Counterfactual Condition (CC)** described above.  
        To evaluate this, compare the new image against the counterfactual caption and assess if it aligns with the intended change from the premise.
        
        ### Response Format:
        Strictly follow the response format below:  
        - Answer with **either** 'yes' or 'no' **on a single line**, formatted as:
        **Answer to Question: [yes/no]**  
        - Provide a **brief** explanation supporting your answer **on a new line**, formatted as:
        **Explanation: [your reasoning]**  

        ### Important Guidelines:
        - **Base your reasoning on both the images and their captions.**  
        - **Do not** include any additional interpretations, explanations, or external information beyond what is explicitly asked.  
        - Maintain conciseness and avoid speculative responses.  
    
    '''