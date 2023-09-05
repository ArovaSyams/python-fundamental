import csv

# =================== READ CSV =====================

# students = []

# with open("File IO/students.csv") as file:
#     for line in file:
        # row = line.rstrip().split(",")
        # name, country = line.rstrip().split(",")
        # students.append({"name": name, "country": country})

        # student = {}
        # student["name"] = name
        # student["country"] = country

        # student = {"name": name, "country": country}

        # print(f"{row[0]} is in {row[1]}")

# def sort_name(student):
#     return student["name"]

# LAMBDA is an anonimous function

# CSV library

# with open("File IO/students.csv") as file:
    # reader = csv.reader(file)
    # mengubah dalam bentuk dict
    # reader = csv.DictReader(file)
    # cara 1
    # for row in reader:
    #     students.append({"name": row[0], "country": row[1]})
    # cara 1.2
    # for name, country in reader:
    #     students.append({"name": name, "country": country})
    # cara 2
    # for row in reader:
    #     students.append({"name": row["name"], "country": row["country"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['country']}")


# ========================== WRITE CSV ==========================

name = input("your name = ")
country = input("Your Country = ")

with open("File IO/students.csv", "a") as file:
    # write
    # writer = csv.writer(file)
    # writer.writerow([name, country])

    # write dict
    writer = csv.DictWriter(file, fieldnames=["name", "country"])
    writer.writerow({"name": name, "country": country})

