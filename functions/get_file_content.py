import os
from .file_utils import get_abs_full_path, is_path_inside_wd, read_file
from config import MAX_CHARS


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
