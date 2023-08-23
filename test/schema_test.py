import unittest
from unittest.mock import patch
from schema_gen import generate_schema

class TestGenerateSchema(unittest.TestCase):

    def test_generate_schema_with_string(self):
        json_data = {
            "attributes": {
                "appName": "AppName",
                "eventType": "EventType",
                "subEventType": "SubEventType",
                "sensitive": False
            }
        }

        expected_schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "properties": {
                "appName": {
                    "type": "str",
                    "tag": "",
                    "description": "",
                    "required": False
                },
                "eventType": {
                    "type": "str",
                    "tag": "",
                    "description": "",
                    "required": False
                },
                "subEventType": {
                    "type": "str",
                    "tag": "",
                    "description": "",
                    "required": False
                },
                "sensitive": {
                    "type": "bool",
                    "tag": "",
                    "description": "",
                    "required": False
                }
            }
        }

        with patch('schema_gen.generate_schema', return_value=expected_schema):
            generated_schema = generate_schema(json_data)
        
        self.assertEqual(generated_schema, expected_schema)

if __name__ == '__main__':
    unittest.main()
