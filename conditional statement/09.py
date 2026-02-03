# A bank offers a loan only to customers who meet certain conditions:
# The customer's salary should be ₹3000 or more.
# They should have aminimum credit score of 700.
# Write a program that checks if a customer is eligible for the loan.

s,c=map(int,input().split())
print("Eligible" if s>=3000 and c>=700 else "Not Eligible")
