import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=None):
    try:
        prefix_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(prefix_path,file_path))

        if os.path.commonpath([prefix_path, target_path]) != prefix_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        try:
            command = [sys.executable, target_path]
            if args:
                command.extend(args)
            executed_run = subprocess.run(command, timeout=30, text=True, cwd=prefix_path, capture_output=True)
            output = []
            if executed_run.returncode != 0:
                output.append(f"Process exited with code {executed_run.returncode}")
            if not executed_run.stderr and not executed_run.stdout:
                output.append("No output produced")
            if executed_run.stdout:
                output.append(f"STDOUT:\n{executed_run.stdout}")
            if executed_run.stderr:
                output.append(f"STDERR:\n{executed_run.stderr}")
            return '\n'.join(output)
        except Exception as e:
            return f"Error: executing Python file: {e}"        
    except Exception as e:
        return e

