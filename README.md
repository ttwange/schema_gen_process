
This is the readme file for the provided assignment where a complete program, best practices adherence, unit tests, and proper submission guidelines. Based on the provided instructions.
<br>

1. **Create the Project Structure:** (\)
   ```plaintext<br>
   project_folder/<br>
   ├── data/<br>
   │   ├── input1.json<br>
   │   ├── input2.json<br>
   │   └── ...<br>
   ├── schema/<br>
   ├── main.py<br>
   ├── schema_gen.py<br>
   ├── tests/<br>
   │   └── schema_test.py<br>
   ├── requirements.txt<br>
   └── README.md<br>
   ```<br>

2. **Setup Virtual Environment:**<br>

   Create and activate a virtual environment as explained earlier.<br>

3. **Install Dependencies:**<br>

   In the virtual environment, install the required dependency using the `requirements.txt` file:<br>

   ```sh<br>
   pip install -r requirements.txt<br>
   ```<br>

   This installs the `jsonschema` library.<br>

4. **Write the `schema_gen.py` File:**<br>

   Write a Python file named `schema_gen.py` that contains the code for reading JSON files, generating schemas, and dumping them. This is where you implement the core logic of your program.<br>

5. **Write Unit Tests:**<br>

   Inside the `tests/` folder, write a Python file named `schema_test.py` to create and run unit tests for your `schema_gen.py` code.<br>

6. **Create `main.py`:**<br>

   Write a Python file named `main.py` in the project folder. This will serve as the entry point to your program. It should call the necessary functions from `schema_gen.py` to generate and save schemas.<br>

By following these steps, you will create a comprehensive solution that meets the requirements for generating JSON schemas, adheres to software best practices and Python coding standards, includes <br>unit tests, and provides clear submission instructions.<br>
#   s c h e m a _ g e n _ p r o c e s s <br>
 
 
**NB**<br>
The program reads JSON files from the `./data/` directory, infers their schema, and saves the inferred schema as a new JSON file in the `./schema/` directory. It uses the `jsonschema` library to <br>validate and generate JSON schemas. You'll need to install this library using `pip install jsonschema`.<br>

Keep in mind that this assumes that the JSON files have a consistent structure and can be treated as dictionaries with nested objects.
