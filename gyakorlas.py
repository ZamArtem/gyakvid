#first_name = "pityu"
#last_name = "szek"
#full_name = first_name + last_name
#print(type(name))
#print("Hello " + full_name)
#age = 21
#age = age + 1
#print("Your age is: " +str (age))
#height = 250.5
#print("Yor height is: " + str(height) + "cm")
#human = True
#print("Are you a human: " +str(human))
#print(type(human))

#name = "Pityu"
#age = 21
#attractive = True
#name, age, attractive   = "Pityu", 21, True
#print(name)
#print(age)
#print(attractive)
#Pityu = 30
#Sanyi = 30
#Kevin = 30 

#Pityu = Sanyi = Kevin = 30

#print(Pityu)
#print(Sanyi)
#print(Kevin)

#name = "Pityu"

#print(len(name))
#print(name.find("P"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha)
#print(name.replace("u","a"))
#print(name * 3)
#name = input("What is your name?: ")
#age = int(input("How old are you?: "))
#height = float(input("How tall are you?: "))

#print("Hello "+ name)
#print("You are " + str(age) + " years old")
#print("You are "+ str(height)+"cm tall")

#def hello(name):
    #print("hello "+name)
    #print("Have a nice day!")


#hello("Artem")
"""
def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum


print(add(1,2,3,4,5,6))
"""
"""
def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.",first="Ar",middle="tem",last="zam")
"""

