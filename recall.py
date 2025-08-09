import json
from g4f.client import Client
client = Client()

debug = False

# Load the correct answers
with open('zero_shot_outputs/correct_answers.json', 'r') as f:
    correct_answers = json.load(f)

# Load the llm responses
def load_llm_response(llm_responses_file_path):
    with open(llm_responses_file_path) as f:
        llm_responses = json.load(f)
        return llm_responses

llm_responses_file_paths = [
    'zero_shot_outputs/outputs6/gpt-4o_llm_responses.json',
    'zero_shot_outputs/outputs6/gemini-pro_llm_responses.json',
    'zero_shot_outputs/outputs6/llama-3.1-70b_llm_responses.json'
]

llm_responses = []
for file_path in llm_responses_file_paths:
    res = load_llm_response(file_path)
    if debug:
        print(file_path.split("/")[1],'has', len(res), 'answers')
    llm_responses.append(res)
    
def calc_recall(llm_responses, total_positives):
    true_positives = 0
    count_deny_service = 0
    for question, correct_answer in correct_answers.items():
        if question in llm_responses:
            llm_answer = llm_responses[question]['llm_answer']
            if "I can't generate an answer" in llm_answer:
                count_deny_service += 1
            if '.' in llm_answer:
                llm_answer = llm_responses[question]['llm_answer'].split(".")[0]
                # llm_answer = llm_responses[question]['llm_answer'].rstrip('.') # remove dot ("2.") if it exists
            if llm_answer == correct_answer:
                true_positives += 1
            else:
                if :
                    print(question, correct_answer)
                    print(llm_responses[question])
                else:
                    continue 
    recall = true_positives / total_positives     
    DoS_ratio = count_deny_service / total_positives
    return recall, DoS_ratio

total_positives = len(correct_answers)
if debug:
    print('there\'re', total_positives, 'correct answers\n')
for llm_response in llm_responses:
    recall, DoS_ratio = calc_recall(llm_response, total_positives)
    print(f'Recall: {recall:.2f}')
    print(f'DoS: {DoS_ratio:.2f}\n')

        