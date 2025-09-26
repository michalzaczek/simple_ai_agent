import os


def get_abs_full_path(working_directory, directory):
    full_path = os.path.join(working_directory, directory)
    abs_full_path = os.path.abspath(full_path)
    return abs_full_path


def is_path_inside_wd(working_directory, abs_full_path):
    abs_working_directory_path = os.path.abspath(working_directory)
    return abs_full_path.startswith(abs_working_directory_path)


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
