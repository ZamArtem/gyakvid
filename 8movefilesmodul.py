import os

source = "copy.txt"
destination = "C:\\Users\\artyx\\OneDrive\\Asztali gép\\test.txt"
# masik merevlemezre nem lehet mozgatni elemeket ezzel a modszerrel
try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")















