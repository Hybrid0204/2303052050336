#
# Write a program that takes the current time (hours in 24-hour format) as input and prints a greeting based on the time (morning, afternoon, evening, or night).

h=int(input())
print("Morning" if h<12 else "Afternoon" if h<17 else "Evening" if h<21 else "Night")
