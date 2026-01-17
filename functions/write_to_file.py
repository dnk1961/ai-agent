import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        prefix_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(prefix_path,file_path))

        if os.path.commonpath([prefix_path, target_path]) != prefix_path:
            return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory"
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        with open(target_path, "w") as file:
            file.write(content)
            return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

    except Exception as e:
        return {e} 
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to a python file provided it exists within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)