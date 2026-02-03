#  Aschool is planning to conduct a special celebration every leap year. Write a program to check if a
# given year is a leap year. The rules for leap years are:
# Ayearisaleapyear ifit is divisible by 4.
# However,if the year is divisible by 100, it is not a leap year unless it is also divisible by 400

y=int(input())
print("Leap Year" if y%400==0 or y%4==0 and y%100!=0 else "Not Leap Year")
