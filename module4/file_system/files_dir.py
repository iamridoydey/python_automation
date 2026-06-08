import os
def mkdir(parent_dir, dir):
    path=os.path.join(parent_dir, dir)
    os.makedirs(path)
    print(f"{dir} successfully created")

def rmdir(parent_dir, dir):
    path=os.path.join(parent_dir, dir)
    os.rmdir(path)
    
def createFile(path, file):
    path = os.path.join(path, file)
    flags=os.O_CREAT | os.O_WRONLY
    permission=0o644
    file = os.open(path, flags, permission)
    os.write(file, b"Hello, World")
    os.close(file)
    
def removeFile(path, file):
    path = os.path.join(path, file)
    os.remove(path)
    
def renameFile(srcPath, desPath):
    os.rename(srcPath, desPath)
    
def joinPath(path, dirORfile):
    return os.path.join(path, dirORfile)
    
if __name__ == "__main__":
    dir="prite"
    parent_dir="/workspaces/python_automation/module4/file_system/"
    
    # create file path
    filePath = os.path.join(parent_dir, dir)
    
    # mkdir(parent_dir, dir)
    # rmdir(parent_dir, dir)
    # createFile(filePath, "index.txt")
    # removeFile(filePath, "rename.txt")
    # renameFile(joinPath(filePath, "index.txt"), joinPath(filePath, "rename.txt"))

