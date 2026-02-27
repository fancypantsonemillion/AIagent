import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'
        
        items = os.listdir(target_dir)
        output = []

        for item in items:
            item_path = os.path.join(target_dir, item)
            stats = os.stat(item_path)
            is_dir = os.path.isdir(item_path)
            size = stats.st_size

            output.append(f"-{item}: file_size={size} bytes, is_dir={is_dir}")
        
        return "/n".join(output)
    
    except Exception as e:
        return f"Error:{str(e)}"
