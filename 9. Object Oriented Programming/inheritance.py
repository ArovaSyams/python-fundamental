class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name is empty")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Proffesor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Kanka")
student = Student("Rahul", "India")
proffesor = Proffesor("Lolay", "Statistic")

print(wizard.name)
print(student.name)
print(proffesor.name)

