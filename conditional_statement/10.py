# A companygives bonuses to employees based on their years of service:
# Less than 5years: Nobonus.
# 5 to 10 years:10% of their annual salary.
# More than 10 years:20% of their annual salary.
# Write a program that calculates the bonus based on years of service.

y,s=map(int,input().split())
print(0 if y<5 else s*0.1 if y<=10 else s*0.2)
