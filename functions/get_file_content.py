import os
from google.genai import types

from .file_utils import get_abs_full_path, is_path_inside_wd, read_file
from config import MAX_CHARS

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)


def get_file_content(working_directory, file_path):
    try:
        abs_full_path = get_abs_full_path(working_directory, file_path)
        if not is_path_inside_wd(working_directory, abs_full_path):
            raise Exception(
                f'Cannot read "{file_path}" as it is outside the permitted working directory'
            )

        if not os.path.isfile(abs_full_path):
            raise Exception(f'File not found or is not a regular file: "{file_path}"')

        file_content = read_file(abs_full_path)

        # Check if content was truncated and add message if needed
        if len(file_content) >= MAX_CHARS:
            file_content += (
                f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            )

        return file_content
    except Exception as e:
        return f"Error: {str(e)}"
