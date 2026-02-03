# Imagine Ram borrowed abookfromthelibrary but returned it late. The library has the following
# rule:
#  If hereturns the bookwithin 5 days of the due date, the fine is ₹5.
#  If hereturns it between 6 to 10 dayslate, the fine is ₹10.
#  If it's more than 10 days late, the fine is ₹15.
# Write a program to calculate the fine based on the number of late days.

d=int(input())
print(5 if d<=5 else 10 if d<=10 else 15)
