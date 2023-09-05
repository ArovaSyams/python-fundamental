grade = int(input("grade: "))

# AND
if grade >= 90 and grade <= 100:
    print("grade A")
elif grade >= 80 and grade < 90:
    print("grade B")
elif grade >= 70 and grade < 80:
    print("grade C")
elif grade >= 60 and grade < 70:
    print("grade D")
else:
    print("grade F")