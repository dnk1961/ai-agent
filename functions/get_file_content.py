import os
from constants import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        prefix_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(prefix_path,file_path))

        if os.path.commonpath([prefix_path, target_path]) != prefix_path:
            return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"
        if not os.path.isfile(target_path):
            return f"Error: File not found or is not a regular file: '{file_path}'"
        with open(target_path, "r") as file:
            file_content = file.read(MAX_CHARS)
            if file.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content
    except Exception as e:
        return f"Error reading file content: {e}"
    
#print(get_file_content("calculator", "lorem.txt"))