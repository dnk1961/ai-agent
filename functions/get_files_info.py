import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        #path prefix /Users/dylankim/Development/ai-agent/
        prefix_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(prefix_path, directory))
        #isvalid_target_dir = os.path.commonpath([prefix_path,target_dir]) == prefix_path
        if os.path.commonpath([prefix_path,target_dir]) != prefix_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        files_list = os.listdir(target_dir)
        files_info = []
        for file in files_list:
            file_path = os.path.join(target_dir,file)
            files_info.append(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
        return '\n'.join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is '.' for current directory)",
            ),
        },
        required=["directory"],
    ),
)