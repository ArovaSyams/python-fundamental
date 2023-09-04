import random

class Home:
    # class variable
    houses = ["Indonesia", "Turki", "Australia"]

    # class method
    @classmethod
    def house(cls, student):
        print(student, "is in", random.choice(cls.houses))


# kita tidak perlu membuat instance
# home = Home()

Home.house("Wifqo")