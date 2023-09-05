# def main():
#     yell("This", "is", "me!")

# def yell(*words):
#     uppercased = [word.upper() for word in words]
#     print(*uppercased)

# main()

#  ex 2

students = [
    {"name": "wifqo", "house": "Indonesia"},
    {"name": "arova", "house": "Indonesia"},
    {"name": "wifqo", "house": "Turki"},
    {"name": "arjaha", "house": "Indonesia"},
]

indonesia = [
    student["name"] for student in students if student["house"] == "Indonesia"
]

print(indonesia)