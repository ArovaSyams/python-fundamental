# advantage for using class = you can handle more in the object rather in dict or list(ex: validation)
class Student:
    # instance method / constructor
    def __init__(self, name, house, mantra):
        # validate
        if not name:
            # make my own error handling
            raise ValueError("name is empty")
        if house not in ["Indonesia", "Turki"]:
            raise ValueError("House Invalid")
        self.name = name
        self.house = house
        self.mantra = mantra

    # change the class object to str format
    def __str__(self):
        return f"{self.name} is in {self.house}"
    
    def kelakuan(self):
        if self.mantra == "lari":
            return "Berlari"


def main():
    student = get_student()
    
    print(student.kelakuan())
    # print(f"{student.name} is in {student.house}")

def get_student():
    name = input("name = ")
    house = input("house = ")
    mantra = input("mantra = ")
    # Constructor
    student = Student(name, house, mantra)
    return student

main()