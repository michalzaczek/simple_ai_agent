import os
import subprocess
import sys
from functions.file_utils import get_abs_full_path, is_path_inside_wd


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = get_abs_full_path(working_directory, file_path)

        # 1) poza working directory
        if not is_path_inside_wd(abs_working_dir, abs_full_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # 2) plik nie istnieje
        if not os.path.exists(abs_full_path):
            return f'Error: File "{file_path}" not found.'

        # 3) nie .py
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        # 4) komenda
        args = [] if args is None else list(map(str, args))
        cmd = [sys.executable, abs_full_path] + args

        # 5) uruchomienie
        result = subprocess.run(
            cmd,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )

        stdout = (result.stdout or "").strip()
        stderr = (result.stderr or "").strip()

        # 6) formatowanie wyjścia
        if not stdout and not stderr:
            return "No output produced."

        parts = []
        if stdout:
            parts.append(f"STDOUT:\n{stdout}")
        if stderr:
            parts.append(f"STDERR:\n{stderr}")
        if result.returncode != 0:
            parts.append(f"Process exited with code {result.returncode}")

        return "\n".join(parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
