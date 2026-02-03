# Write a program to simulate a simple ATM that allows the user to check the balance, withdraw money, and deposit money using conditional statements.

b=int(input());c=input();a=int(input())
print(b if c=="check" else b-a if c=="withdraw" else b+a)
