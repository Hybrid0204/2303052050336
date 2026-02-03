# Imagine Mahesh is playing a game where he haveto guess a magic number.The game gives you
# hints:
# If theguessednumberis less than the magic number, it prints "Too low!"
# If it's higher, it prints "Too high!"
# If it's correct, it congratulates you.
# Write a program to simulate one guess.

g,m=map(int,input().split())
print("Too low!" if g<m else "Too high!" if g>m else "Correct!")