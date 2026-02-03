#  Write a program to check whether a character is uppercase, lowercase, a digit, or a special character.


c=input()
print("Uppercase" if c.isupper() else "Lowercase" if c.islower() else "Digit" if c.isdigit() else "Special")
