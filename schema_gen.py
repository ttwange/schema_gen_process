import json

def generate_schema(json_data):
    schema = {"$schema": "http://json-schema.org/draft-07/schema#"}
    
    def explore(data, path=None):
        if isinstance(data, dict):
            if path is None:
                path = []
                
            for key, value in data.items():
                new_path = path + [key]
                if isinstance(value, dict):
                    explore(value, new_path)
                elif isinstance(value, list):
                    if all(isinstance(item, str) for item in value):
                        schema["properties"][new_path[-1]] = {
                            "type": "array",
                            "items": {"type": "string", "enum": value},
                            "tag": "",
                            "description": "",
                            "required": False  # Add the "required" field
                        }
                    elif all(isinstance(item, dict) for item in value):
                        schema["properties"][new_path[-1]] = {
                            "type": "array",
                            "items": generate_schema(value[0]),
                            "tag": "",
                            "description": "",
                            "required": False  # Add the "required" field
                        }
                else:
                    schema["properties"][new_path[-1]] = {
                        "type": type(value).__name__.lower(),
                        "tag": "",
                        "description": "",
                        "required": False  # Add the "required" field
                    }
    
    schema["properties"] = {}
    explore(json_data["attributes"])
    return schema
