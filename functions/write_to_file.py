import os

def write_to_file(working_directory, file_path, content):
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