students = [
    {"name": "wifqo", "house": "Indonesia"},
    {"name": "arova", "house": "Indonesia"},
    {"name": "wifqo", "house": "Turki"},
    {"name": "arjaha", "house": "Indonesia"},
]

# can use with separated function or with lambda
def is_indonesia(s):
    return s["house"] == "Indonesia"

indonesia = filter(lambda s: s["house"] == "Indonesia", students)

for ind in indonesia:
    print(ind["name"])