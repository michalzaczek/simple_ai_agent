import os
from functions.file_utils import get_abs_full_path, is_path_inside_wd


def get_file_content(working_directory, file_path):
    try:
        abs_full_path = get_abs_full_path(working_directory, file_path)
        if not is_path_inside_wd(working_directory, abs_full_path):
            raise Exception(
                f'Cannot read "{file_path}" as it is outside the permitted working directory'
            )

        if not os.path.isfile(abs_full_path):
            raise Exception(f'File not found or is not a regular file: "{file_path}"')
    except Exception as e:
        return f"Error: {str(e)}"


print(get_file_content())
