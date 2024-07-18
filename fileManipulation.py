import os
import shutil

def organize_png_files(directory: str):
    """move png files in subfolder, 9 files in each subfolders

    Args:
        directory (str): root working directory
    """
    files_with_underscore = []
    files_without_underscore = []
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            if '_' in filename:
                files_with_underscore.append(filename)
            else:
                files_without_underscore.append(filename)
    def create_subfolders_and_move_files(files):
        for i in range(0, len(files), 9):
            num_files_in_subfolder = len(files[i:i + 9])
            subfolder_name = f"Page {i // 9 + 1}"
            if num_files_in_subfolder != 9:
                subfolder_name += f" _ {num_files_in_subfolder}"
            subfolder_path = os.path.join(directory, subfolder_name)
            os.makedirs(subfolder_path, exist_ok=True)
            for file in files[i:i + 9]:
                shutil.move(os.path.join(directory, file), os.path.join(subfolder_path, file))
    create_subfolders_and_move_files(files_without_underscore)
    create_subfolders_and_move_files(files_with_underscore)

def get_all_png(directory: str)->list:
    """from a folder collect complete path of all png files

    Args:
        directory (str): root working directory

    Returns:
        list: list of complete path 
    """
    pngFiles = []
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            pngFiles.append(f"{directory}/{filename}")
    return pngFiles
