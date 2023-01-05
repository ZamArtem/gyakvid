

#lvl 1
"""
students = ("Patrick","Zam Art","Gipsz Jakab","Gipsz Rozália")

#students.sort(reverse=True)   [csak lista]
sorted_students = sorted(students)
for i in sorted_students:
    print(i)
"""

students = [("Patrick", "F", 60),
            ("Zam Art", "A", 33),
            ("Gipsz Jakab", "D", 36),
            ("Gipsz Rozália", "B", 20)]


grade = lambda grades:grades[1]
# students.sort(key=grade,reverse=True)
sorted_students = sorted(students,key=grade)

for i in students:
    print(i)