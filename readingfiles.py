try:
    with open("C:\\Users\\artyx\\OneDrive\\Asztali gép\\teszt.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
