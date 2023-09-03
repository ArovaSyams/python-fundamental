# advantage for using class = you can handle more in the object rather in dict or list(ex: validation)
class Student:
    # instance method / constructor
    def __init__(self, name, house):     
        self.name = name
        self.house = house

    # change the class object to str format
    def __str__(self):
        return f"{self.name} is in {self.house}"
    
    # Getter & Setter

    # getter
    @property
    def name(self):
        return self._name
    # setter
    @name.setter
    def name(self, name):
        if not name:
            # make my own error handling
            raise ValueError("name is empty")
        self._name = name

    # getter
    @property
    def house(self):
        return self._house
    # setter
    @house.setter
    def house(self, house):
        if house not in ["Indonesia", "Turki"]:
            raise ValueError("House Invalid")
        self._house = house



def main():
    student = get_student()
    student._house = "Bengkulu"
    print(student)

def get_student():
    name = input("name = ")
    house = input("house = ")
    # Constructor
    student = Student(name, house)
    return student

main()