#!/bin/bash

# python g4f_models.py

# Session crass-zero_shot
# tmux new-session -d -s crass-zero_shot
# tmux send-keys -t crass-zero_shot "bash" C-m
# tmux send-keys -t crass-zero_shot "conda activate cf" C-m
# tmux send-keys -t crass-zero_shot "python -u inference.py --dataset CRASS --mode zero_shot --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3,claude-3.7-sonnet,claude-3-sonnet,blackboxai-pro,blackboxai,llava-1.5-7b-hf | tee crass-zero_shot.log" C-m
# tmux send-keys -t crass-zero_shot "wait" C-m
# tmux send-keys -t crass-zero_shot "python cf_evaluation.py --dataset CRASS --mode zero_shots" C-m

# Session crass-few_shot
# tmux new-session -d -s crass-few_shots
# tmux send-keys -t crass-few_shot "bash" C-m
# tmux send-keys -t crass-few_shot "conda activate cf" C-m
# tmux send-keys -t crass-few_shot "python -u inference.py --dataset CRASS --mode few_shots --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3,claude-3.7-sonnet,claude-3-sonnet,blackboxai-pro,blackboxai,llava-1.5-7b-hf | tee crass-few_shots.log" C-m
# tmux send-keys -t crass-few_shot "wait" C-m
# tmux send-keys -t crass-few_shot "python cf_evaluation.py --dataset CRASS --mode few_shots" C-m

# Session crass-cot
# tmux new-session -d -s crass-cot
# tmux send-keys -t crass-cot "bash" C-m
# tmux send-keys -t crass-cot "conda activate cf" C-m
# tmux send-keys -t crass-cot "python -u inference.py --dataset CRASS --mode CoT --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3,claude-3.7-sonnet,claude-3-sonnet,blackboxai-pro,blackboxai,llava-1.5-7b-hf | tee crass-cot.log" C-m
# tmux send-keys -t crass-cot "wait" C-m
# tmux send-keys -t crass-cot "python cf_evaluation.py --dataset CRASS --mode CoT" C-m

# Session cvqa-bool-zero_shot
# tmux new-session -d -s cvqa-bool-zero_shot
# tmux send-keys -t cvqa-bool-zero_shot "bash" C-m
# tmux send-keys -t cvqa-bool-zero_shot "conda activate cf" C-m
# tmux send-keys -t cvqa-bool-zero_shot "python -u inference.py --dataset CVQA-Boolean --mode zero_shots --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3,claude-3.7-sonnet,claude-3-sonnet,blackboxai-pro,blackboxai,llava-1.5-7b-hf | tee cvqa-bool-zero_shot.log" C-m
# tmux send-keys -t cvqa-bool-zero_shot "wait" C-m
# tmux send-keys -t cvqa-bool-zero_shot "python cf_evaluation.py --dataset CVQA-Boolean --mode zero_shot" C-m

# Session cvqa-bool-few_shots
# tmux new-session -d -s cvqa-bool-few_shots
# tmux send-keys -t cvqa-bool-few_shots "bash" C-m
# tmux send-keys -t cvqa-bool-few_shots "conda activate cf" C-m
# tmux send-keys -t cvqa-bool-few_shots "python -u inference.py --dataset CVQA-Boolean --mode few_shots --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3,claude-3.7-sonnet,claude-3-sonnet,blackboxai-pro,blackboxai,llava-1.5-7b-hf | tee cvqa-bool-few_shots.log" C-m
# tmux send-keys -t cvqa-bool-few_shots "wait" C-m
# tmux send-keys -t cvqa-bool-few_shots "python cf_evaluation.py --dataset CVQA-Boolean --mode few_shots" C-m

# Session cvqa-bool-cot
# tmux new-session -d -s cvqa-bool-cot
# tmux send-keys -t cvqa-bool-cot "bash" C-m
# tmux send-keys -t cvqa-bool-cot "conda activate cf" C-m
# tmux send-keys -t cvqa-bool-cot "python -u inference.py --dataset CVQA-Boolean --mode CoT --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3,claude-3.7-sonnet,claude-3-sonnet,blackboxai-pro,blackboxai,llava-1.5-7b-hf | tee cvqa-bool-cot.log" C-m
# tmux send-keys -t cvqa-bool-cot "wait" C-m
# tmux send-keys -t cvqa-bool-cot "python cf_evaluation.py --dataset CVQA-Boolean --mode CoT" C-m


# Session clomo-zero_shot
# tmux new-session -d -s clomo-zero_shot
# tmux send-keys -t clomo-zero_shot "bash" C-m
# tmux send-keys -t clomo-zero_shot "conda activate cf" C-m
# tmux send-keys -t clomo-zero_shot "python -u inference.py --dataset CLOMO --mode zero_shot --models gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3 | tee clomo-zero_shot.log" C-m
# tmux send-keys -t clomo-zero_shot "wait" C-m
# tmux send-keys -t clomo-zero_shot "python cf_evaluation.py --dataset CLOMO --mode zero_shots" C-m

# Session clomo-CoT
# tmux new-session -d -s clomo-CoT
# tmux send-keys -t clomo-CoT "bash" C-m
# tmux send-keys -t clomo-CoT "conda activate cf" C-m
# tmux send-keys -t clomo-CoT "python -u inference.py --dataset CLOMO --mode CoT --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3 | tee clomo-CoT.log" C-m
# tmux send-keys -t clomo-CoT "wait" C-m
# tmux send-keys -t clomo-CoT "python cf_evaluation.py --dataset CLOMO --mode CoT" C-m

# Session arith-16-CoT
# tmux new-session -d -s arith-16-CoT
# tmux send-keys -t arith-16-CoT "bash" C-m
# tmux send-keys -t arith-16-CoT "conda activate cf" C-m
# tmux send-keys -t arith-16-CoT "python -u inference.py --dataset Arithmetic-Base-16 --mode CoT --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3 | tee arith-16-CoT.log" C-m
# tmux send-keys -t arith-16-CoT "wait" C-m
# tmux send-keys -t arith-16-CoT "python cf_evaluation.py --dataset Arithmetic-Base-16 --mode CoT" C-m



# Session clomo-zero_shot
# tmux new-session -d -s code-exe-zero_shot
# tmux send-keys -t code-exe-zero_shot "bash" C-m
# tmux send-keys -t code-exe-zero_shot "conda activate cf" C-m
# tmux send-keys -t code-exe-zero_shot "python -u inference.py --dataset Code-Exe --mode zero_shot --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3 | tee code-exe-zero_shot.log" C-m
#tmux send-keys -t code-exe-zero_shot "wait" C-m
#tmux send-keys -t code-exe-zero_shot "python cf_evaluation.py --dataset Code-Exe --mode zero_shots" C-m


# Session clomo-zero_shot
# tmux new-session -d -s code-exe-CoT
# tmux send-keys -t code-exe-CoT "bash" C-m
# tmux send-keys -t code-exe-CoT "conda activate cf" C-m
# tmux send-keys -t code-exe-CoT "python -u inference.py --dataset Code-Exe --mode CoT --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3 | tee code-exe-CoT.log" C-m
# tmux send-keys -t code-exe-CoT "wait" C-m
# tmux send-keys -t code-exe-CoT "python cf_evaluation.py --dataset Code-Exe --mode CoT" C-m





# tmux new-session -d -s code-sum-CoT
# tmux send-keys -t code-sum-CoT "bash" C-m
# tmux send-keys -t code-sum-CoT "conda activate cf" C-m
# tmux send-keys -t code-sum-CoT "python -u inference.py --dataset Code-Sum --mode CoT --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3 | tee code-sum-CoT.log" C-m



# Session syntax_zero_shot
# tmux new-session -d -s syntax-CoT
# tmux send-keys -t syntax-CoT "bash" C-m
# tmux send-keys -t syntax-CoT "conda activate cf" C-m
# tmux send-keys -t syntax-CoT "python -u inference.py --dataset Syntax --mode CoT --models gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3 | tee syntax-CoT.log" C-m

tmux new-session -d -malalgo-zero_shot
tmux send-keys -t syntax-zero_shot "bash" C-m
tmux send-keys -t syntax-zero_shot "conda activate cf" C-m
tmux send-keys -t syntax-zero_shot "python -u inference.py --dataset Syntax --mode zero_shot --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3 | tee syntax-zero_shot.log" C-m



# Create a new tmux session named 'experiment' and run commands inside it
# tmux new-session -d -s experiment

# Run bash in the tmux session
# tmux send-keys -t experiment "bash" C-m

# Activate the Conda environment
# tmux send-keys -t experiment "conda activate cf" C-m

# Run the inference command and log the output
# tmux send-keys -t experiment "python -u inference.py --dataset CRASS --models gpt-4,gpt-4o,gpt-4o-mini,gemini-2.0-pro,gemini-2.0-flash,llama-3.1-405b,llama-3.1-70b,llama-3.1-8b,qwen-2-72b,deepseek-v3,claude-3.7-sonnet,claude-3-sonnet,blackboxai-pro,blackboxai --mode few_shots | tee output.log" C-m
# tmux send-keys -t experiment "python -u inference.py --dataset CRASS --models gpt-4 --mode few_shots | tee output.log" C-m

# Wait for the previous command to complete
# tmux send-keys -t experiment "wait" C-m

# Run the evaluation command
# tmux send-keys -t experiment "python cf_evaluation.py --dataset CRASS --mode few_shots" C-m

# Attach to the tmux session to monitor progress
# tmux attach -t experiment



