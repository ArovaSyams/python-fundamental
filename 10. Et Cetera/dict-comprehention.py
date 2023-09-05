students = ["wifqo", "arova", "syams"]

# replace dict for the brand new one 

# turki = [{"name": student, "house": "turki"} for student in students]
turki = {student: "turki" for student in students}

print(turki)
