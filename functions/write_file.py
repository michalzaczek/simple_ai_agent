import os
from functions.file_utils import get_abs_full_path, is_path_inside_wd


def write_file(working_directory, file_path, content):
    try:
        abs_full_path = get_abs_full_path(working_directory, file_path)

        if not is_path_inside_wd(working_directory, abs_full_path):
            raise Exception(
                f'Cannot write to "{file_path}" as it is outside the permitted working directory'
            )

        # Create directory if it doesn't exist
        directory = os.path.dirname(abs_full_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Write the file (creates it if it doesn't exist)
        with open(abs_full_path, "w", encoding="utf-8") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {str(e)}"
