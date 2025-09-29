import os
from google.genai import types
from .get_files_info import get_files_info
from .get_file_content import get_file_content
from .run_python_file import run_python_file
from .write_file import write_file


def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    # Make a copy to avoid modifying original
    function_args = function_call_part.args.copy()

    # Print function call info
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    # Add working_directory to the args
    working_directory = "./calculator"
    function_args["working_directory"] = working_directory

    # Dictionary mapping function names to actual functions
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    # Check if function exists
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    # Call the function with keyword arguments
    try:
        function_result = function_map[function_name](**function_args)
    except Exception as e:
        function_result = f"Error calling function: {str(e)}"

    # Return types.Content with function response
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
