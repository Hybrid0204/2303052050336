# Write a program that takes a temperature in Celsius and converts it to Fahrenheit, then checks if it is hot, moderate, or cold based on the temperature.

c=int(input());f=c*9/5+32
print("Hot" if f>85 else "Moderate" if f>=60 else "Cold")
