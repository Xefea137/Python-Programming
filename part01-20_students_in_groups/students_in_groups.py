"""
Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

How many students on the course? 8
Desired group size? 4
Number of groups formed: 2

How many students on the course? 11
Desired group size? 3
Number of groups formed: 4
"""

students = int(input("How many students on the course? "))
size = int((input("Desired group size ")))
group = students/size
if group %2 != 0:
    group += 1

#print(f"Number of groups formed: {group//1}")
print(f"Number of groups formed: {int(group)}")