import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MODEL_NAME, SYSTEM_PROMPT
from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    sys_args = sys.argv
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    if len(sys_args) < 2:
        print("Error: no prompt provided!")
        sys.exit(1)

    user_prompt = sys_args[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT
        ),
    )

    # Handle function calls if they exist
    function_calls = response.function_calls
    if function_calls:
        for fc in function_calls:
            function_name = fc.name
            function_args = fc.args

            # if len(sys_args) > 2 and sys_args[2] == "--verbose":
            print(f"Calling function: {function_name} with args: {function_args}")

            # Execute the function
            if function_name == "get_files_info":
                working_directory = os.getcwd()
                directory = function_args.get("directory", ".")
                result = get_files_info(working_directory, directory)
                print(result)
            else:
                print(f"Unknown function: {function_name}")
    else:
        # Print the response text if no function calls
        if response.text:
            print(response.text)

        # Handle verbose output
        # if len(sys_args) > 2 and sys_args[2] == "--verbose":
        usage_metadata = response.usage_metadata
        prompt_tokens = usage_metadata.prompt_token_count
        response_tokens = usage_metadata.candidates_token_count
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
