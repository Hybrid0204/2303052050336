# Imagine Sai at a national park. The park has a new thrilling ride with a strict requirement that only people aged 12 and above, and with a height of 150 cm or more, can go on it. Write a program to check if Sai is eligible for the ride.

a,h=map(int,input().split())
print("Eligible" if a>=12 and h>=150 else "Not Eligible")