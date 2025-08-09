from g4f.client import Client
client = Client()
models = [
    'gpt-4',
    'gpt-4o',
    'gpt-4o-mini',
    # Google
    'gemini-2.0-pro',
    'gemini-2.0-flash',
     # Meta
    'llama-3.1-405b',
    'llama-3.1-70b',# llama-3.2-90b
    'llama-3.1-8b', # llama-3.2-11b
    'llama-3.2-90b', # not available
    'llama-3.2-11b', # not available 
    # Alibaba
    'qwen-2-72b',
    # Deepseek
    'deepseek-v3',
    # Anthropic
    'claude-3.7-sonnet',
    'claude-3-sonnet',
    # Blackbox AI
    'blackboxai-pro', 
    'blackboxai',
    # Cohere
    'command-r'
    '''
    'command-r-plus',
    'qwen-2.5-coder',
    'gemini-1.5-flash',
    'gemini-1.5-pro',
    # Claude models
    'claude-3.5-sonnet',
    'claude-3-opus',
    'claude-3-haiku',
    'claude-3-sonnet',
    'claude-instant',
    # Anthropic models
    'claude-3.7-sonnet',
    # Google models
    'gemini-1.0-pro',
    'palm-2',
    # Mistral models
    'mistral-7b',
    'mistral-8x7b',
    'mixtral-8x7b',
    'mistral-medium',
    'mistral-small',
    'mistral-large',
    # Cohere models
    'command',
    'command-light',
    'command-nightly',
    # Anthropic additional models
    'claude-instant-1.2',
    # Other providers
    'yi-34b',
    'yi-6b',
    'falcon-7b',
    'falcon-40b',
    'qwen-14b',
    'qwen-7b',
    'deepseek-coder',
    'deepseek-v3'
    'j2-ultra',
    'j2-mid'
    '''
]
print("Test the availability of models...\n")
available_models = []
for model in models:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "Test if the model is available"}],
            timeout=60
        ).choices[0].message.content.strip()
        print(f"Model {model} is available, Response:{response}")
        available_models.append(model)
    except Exception as e:
        print(f"Model {model} is not available, Error:{e}")
print("\nList of available models:", available_models)

