"""
Please write a program which asks the user for their name and year of birth. The program then prints out a message as follows:

What is your name? Frances Fictitious
Which year were you born? 1990
Hi Frances Fictitious, you will be 31 years old at the end of the year 2021
"""

name = input("What is your name? ")
age = int(input("Which year were you born in? "))
print(f"Hi {name}, you will be {2021-age} years old at the end of the year 2021")