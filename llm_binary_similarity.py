
from g4f.client import Client

def g4f_generate(prompt):
    client = Client()
    response = None
    for llm in [
        'gpt-4o',
        'gpt-4',
        'blackboxai-pro',
        'blackboxai',
        'gpt-4o-mini',
        
        "gemini-1.5-pro", 
        "gemini-1.5-flash", 
        
        'llama-3.1-405b',
        'llama-3.1-70b',
        'llama-3.1-8b',

        'claude-3.5-sonnet',
    ]:
        print('calling', llm)
        try:
            response = client.chat.completions.create(
                model=llm,
                messages=[
                    {"role": "user", "content":
                    prompt}],
                timeout=60,
                # Add any other necessary parameters
            ).choices[0].message.content.strip()
        except:
            continue
        if response is not None and \
            'sorry' not in response and \
            'cannot' not in response  and \
            'rate limit' not in response and \
            "can't" not in response and \
            'not safe' not in response and \
            "don't know" not in response and \
            "403 Forbidden" not in response and \
            'invisible' not in response and \
            'try unlimited chat' not in response and \
            len(response) > 0:
            return response
        else: 
            print('-'*100)
            print(response)
            print('-'*100)
            
    return None


def llm_binary_similarity(resp: str, ref: str):
    prompt = f"""
    Below I will give you a pair of 'generated response' and the 'reference' texts. Determine if they are describing the same underlying topics or objects. Focus on the roughly semantic similarity rather than exact wording. 
    
    Consider the following:

    - Are synonyms or paraphrases used to express similar concepts?
    - Is the overall intent and context similar?
    - Are there any subtle nuances that change the meaning, or is the difference purely stylistic?
    
    Do not provide explanations or additional text. Respond strictly with 'Yes' or 'No'.
    
    **Generated Response:**
    {resp}
    
    **Reference:**
    {ref}
    
    **Your Answer (Yes or No):**
    """
    rst = g4f_generate(prompt)
    # logging.info(">>> LLM response:", resp)
    # logging.info("\n>>> Reference:", ref)
    # logging.info('\n>>> LLM judgement:', rst)
    return not('no' in rst or 'No' in rst or 'NO' in rst)
