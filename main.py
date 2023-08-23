import os
import json
from schema_gen import generate_schema

file_path = r'.\data' 

def read_json_file(data):
    with open(data, 'r') as file:
        return json.load(file)

def dump_schema(schema, output_path):
    with open(output_path, 'w') as file:
        json.dump(schema, file, indent=4)

def main():
    input_folder = './data/'
    output_folder = './schema/'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.json', '_schema.json'))
            
            json_data = read_json_file(input_path)
            inferred_schema = generate_schema(json_data) 
            dump_schema(inferred_schema, output_path)
            print(f"Schema for {filename} generated")

if __name__ == "__main__":
    main()
