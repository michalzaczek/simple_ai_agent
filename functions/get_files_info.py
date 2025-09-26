import os


def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        abs_full_path = os.path.abspath(full_path)
        abs_working_directory_path = os.path.abspath(working_directory)

        if not abs_full_path.startswith(abs_working_directory_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'

        return list_dir_to_str(abs_full_path)
    except Exception as e:
        return f"Error: {str(e)}"


def list_dir_to_str(path):
    try:
        dir_str = ""
        for f_name in os.listdir(path):
            f_path = os.path.join(path, f_name)
            f_size = os.path.getsize(f_path)
            f_isdir = os.path.isdir(f_path)
            f_str = f"- {f_name}: file_size={f_size} bytes, is_dir={f_isdir}\n"
            dir_str += f_str

        return dir_str
    except Exception as e:
        return f"Error: {str(e)}"
