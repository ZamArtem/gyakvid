# filter()


friends = [("Kristof",19),
           ("Balazs",18),
           ("Levi",17),
           ("Gipsz Rozália", 16),
           ("Csongor", 20),
           ("Gipsz Jakab", 21)]

        

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age,friends))

for i in drinking_buddies:
    print(i)