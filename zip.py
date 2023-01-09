#zip(*iterables)

"""
usernames = ["Dude","ZamArt","GipszJ"]
passwords = ("p@assword","abc123","guest")

users = zip(usernames,passwords)

for i in users:
    print(i)

print(type(users))

users = dict(zip(usernames,passwords))

for key,value in users.items():
    print(key + ":" + value)

print(type(users))
"""

usernames  = ["Dude","ZamArt","GipszJ"]
passwords  = ("p@assword","abc123","guest")
login_date = ["1/1/2021","1/1/2021","1/3/2021"]


users = zip(usernames,passwords,login_date)

for i in users:
    print(i)