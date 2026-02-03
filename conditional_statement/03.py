# Ateacher wants a quick way tocheck a student's grade based on marks:
# Ifthemarksare90orabove, the grade is 'A'.
# Ifthemarksarebetween 80and89,the grade is 'B'.
# Ifthemarksarebetween 70and79,the grade is 'C'.
# Ifthemarksarebetween 60and69,the grade is 'D'.
# Below60isafailing grade, 'F'.
# Write a program to assign a grade based on the student's marks.

m=int(input())
print("A" if m>=90 else "B" if m>=80 else "C" if m>=70 else "D" if m>=60 else "F")