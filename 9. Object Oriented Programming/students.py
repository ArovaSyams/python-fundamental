# def main():
#     students = get_student()
#     print(f"{students[0]} is in {students[1]}")


# def get_student():
    # name = input("name: ")
    # house = input("house: ")
    # Tuples = list yang immutable(tidak bisa diubah)
    # return (name, house)




class Student:
    ...

# dict
def main():
    students = get_student()
    
    print(f"{students.name} is in {students.house}")

def get_student():
    # student = {}
    # student["name"] = input("name = ")
    # student["house"] = input("House = ")
    # =========
    # name = input("name: ")
    # house = input("House: ")
    # return {"name": name, "house": house}

    # ======= with class ====
    # student = Student()
    # student.name = input("name: ")
    # student.house = input("house: ")
    # //////
    name = input("name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__=="__main__":
    main()