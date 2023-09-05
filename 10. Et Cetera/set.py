students = [
    {"name": "wifqo", "house": "Bengkulu"},
    {"name": "wifqo", "house": "Bengkulu"},
    {"name": "wifqo", "house": "Malang"},
    {"name": "wifqo", "house": "Jombang"},
    {"name": "wifqo", "house": "Jombang"},
]

houses = set()
for student in students:
    if student["house"] not in houses:
        houses.add(student["house"])

for house in houses:
    print(house)