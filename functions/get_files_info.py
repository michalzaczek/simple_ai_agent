import os
from google.genai import types
from .file_utils import get_abs_full_path, is_path_inside_wd, list_dir_to_str

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


def get_files_info(working_directory, directory="."):
    try:
        abs_full_path = get_abs_full_path(working_directory, directory)

        if not is_path_inside_wd(working_directory, abs_full_path):
            raise Exception(
                f'Cannot list "{directory}" as it is outside the permitted working directory'
            )

        if not os.path.isdir(abs_full_path):
            raise Exception(f'"{directory}" is not a directory')

        return list_dir_to_str(abs_full_path)
    except Exception as e:
        return f"Error: {str(e)}"
