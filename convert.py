from pathlib import Path
import shutil
import os

def convert_starbound(in_path, out_path):
    os.chdir(in_path)
    print(os.getcwd())
    for folder in os.listdir():
        folder_name, folder_ext = os.path.splitext(folder)
        for file in os.listdir(folder):
            if file == None:
                continue
            file_name, file_ext = os.path.splitext(file)
            shutil.copy(Path(folder).absolute().joinpath(file), out_path)
            os.chdir(out_path)
            for new_rename in os.listdir():
                copy_name, copy_ext = os.path.splitext(new_rename)
                new_name = f"{folder_name}{file_ext}"
                if copy_name == "contents":
                    os.rename(new_rename, new_name)
            os.chdir(in_path)

def convert_clear(in_path):
    os.chdir(in_path)
    for extra in os.listdir():
        shutil.rmtree(extra)