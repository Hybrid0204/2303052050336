# Alocal shop offers discounts based on the total purchase amount:
# If thepurchase is ₹1000 or more, you get a 10% discount.
# If thepurchase is ₹2000 or more, you get a 20% discount.
# If thepurchase is ₹3000 or more, you get a 30% discount.
# Write a program that calculates the final price after applying the discount.

p=int(input())
d=0.3 if p>=3000 else 0.2 if p>=2000 else 0.1 if p>=1000 else 0
print(p-p*d)
