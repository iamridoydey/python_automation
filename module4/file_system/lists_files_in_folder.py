import os

def list_files_in_folder(path: str): 
    try:
        files = os.listdir(path)
        return files, None
    except FileNotFoundError:
        return None, "File not found"
    except PermissionError:
        return None, "Permission denied"
    
    
if __name__ == "__main__":
    files, error = list_files_in_folder("/workspaces")
    print("Files: ", files)
    print("Error: ", error)