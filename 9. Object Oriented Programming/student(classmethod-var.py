# advantage for using class = you can handle more in the object rather in dict or list(ex: validation)
class Student:
    # instance method / constructor
    def __init__(self, name, house):     
        self.name = name
        self.house = house

    # change the class object to str format
    def __str__(self):
        return f"{self.name} is in {self.house}"

    @classmethod
    def get(cls):
        name = input("name: ")
        house = input("house: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__=="__main__":
    main()