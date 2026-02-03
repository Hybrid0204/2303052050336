# A cinemaoffers discounts based on age:
# Children(age below 12) get a 50% discount.
# Seniorcitizens (age 60 and above) get a 30% discount.
# Othershavetopaythefull ticket price.
# Write a program to determine the final ticket price for a given age, assuming the full price is ₹20.


a=int(input())
print(10 if a<12 else 14 if a>=60 else 20)
