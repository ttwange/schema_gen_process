
This is the readme file for the provided assignment where a complete program, best practices adherence, unit tests, and proper submission guidelines. Based on the provided instructions.
<br>

1. **Create the Project Structure:**

   ```plaintext
   project_folder/
   ├── data/
   │   ├── input1.json
   │   ├── input2.json
   │   └── ...
   ├── schema/
   ├── main.py
   ├── schema_gen.py
   ├── tests/
   │   └── schema_test.py
   ├── requirements.txt
   └── README.md
   ```

2. **Setup Virtual Environment:**

   Create and activate a virtual environment as explained earlier.

3. **Install Dependencies:**

   In the virtual environment, install the required dependency using the `requirements.txt` file:

   ```sh
   pip install -r requirements.txt
   ```

   This installs the `jsonschema` library.

4. **Write the `schema_gen.py` File:**

   Write a Python file named `schema_gen.py` that contains the code for reading JSON files, generating schemas, and dumping them. This is where you implement the core logic of your program.

5. **Write Unit Tests:**

   Inside the `tests/` folder, write a Python file named `schema_test.py` to create and run unit tests for your `schema_gen.py` code.

6. **Create `main.py`:**

   Write a Python file named `main.py` in the project folder. This will serve as the entry point to your program. It should call the necessary functions from `schema_gen.py` to generate and save schemas.

By following these steps, you will create a comprehensive solution that meets the requirements for generating JSON schemas, adheres to software best practices and Python coding standards, includes unit tests, and provides clear submission instructions.
#   s c h e m a _ g e n _ p r o c e s s 
 
 
**NB**
The program reads JSON files from the `./data/` directory, infers their schema, and saves the inferred schema as a new JSON file in the `./schema/` directory. It uses the `jsonschema` library to validate and generate JSON schemas. You'll need to install this library using `pip install jsonschema`.

Keep in mind that this assumes that the JSON files have a consistent structure and can be treated as dictionaries with nested objects.
