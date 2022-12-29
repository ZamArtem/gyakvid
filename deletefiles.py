import os
import shutil

path = "empty_folder"

try:
    #os.remove(path)        #delete files  
    #os.rmdir(path)         #delete an empty directory
    #shutil.rmtree(path)    #delete a directory containing files
    a = 1
except FileNotFoundError:
    print("That file is not found")
except PermissionError:
    print("You do not have a permission to delete that")
except OSError:
    print("You can not delete this there is files inside")
else:
    print(path+" was deleted")
