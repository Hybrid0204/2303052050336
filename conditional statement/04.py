# Imagine Abhi is building a weather station, and he want to display a message based on the current
# temperature:
# If thetemperature is below 0°C, it's "Freezing".
# If it's between 0°C and 10°C, it's "Very Cold".
# If it's between 11°C and 20°C, it's "Cold".
# If it's between 21°C and 30°C, it's "Warm".
# If it's above 30°C, it's "Hot".
# Write a program to check the temperature status.

t=int(input())
print("Freezing" if t<0 else "Very Cold" if t<=10 else "Cold" if t<=20 else "Warm" if t<=30 else "Hot")
