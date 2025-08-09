import g4f
from g4f.client import Client
from PIL import Image
import csv
import pandas as pd

prompt_template = """
 ### Context:
        Read this image.
 ### 

"""

# load dataset
file_path = 'data/real_questions.csv'
data = {}
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    count = 0
    for row in csv_reader:
        count += 1
        image_name = row['file_name']
        data[image_name] = {
            'query': row['query'],
            'answer': row['answer'],
            'new query': row['new query'],
            'new answer': row['new answer'],
            'type': row['type']
        }
        
df = pd.read_csv(file_path)
image_name, query, answer, new_query, new_answer, type = df['file_name'], df['query'], df['answer'], df['new query'], df['new answer'], df['type']
count = 0
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        record_count += 1
        image_name, query, answer, new_query, new_answer, type = df.iloc[0]["file_name"], df.iloc[0]["query"], df.iloc[0]["answer"], df.iloc[0]["new query"], df.iloc[0]["new answer"], df.iloc[0]["type"]

    print(f"There're {len(image_name)} examples read from the input file")

image_name, query, answer, new_query, new_answer, type = df.iloc[0]["file_name"], df.iloc[0]["query"], df.iloc[0]["answer"], df.iloc[0]["new query"], df.iloc[0]["new answer"], df.iloc[0]["type"]
image_folder = "data/real_images"  # Update with the correct path
image_path = f"{image_folder}/{image_name}"
image = Image.open(image_path)
print(f"Processing {image_name} with query: {query}")

image_path = "data/real_images"