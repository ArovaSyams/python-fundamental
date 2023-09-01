name = input("your name: ")

# Match

match name:
    case "Rava" | "Rama":
        print("family")
    case "Rafi":
        print("friend")
    case _:
        print("anoying")
