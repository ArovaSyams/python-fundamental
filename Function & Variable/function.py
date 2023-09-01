# def main():
#     name = input("What is your name? ")
#     hello(name)

# def hello(to):
#     print("Hello", to)

# main()

# return

def main():
    x = int(input("number = "))
    print("the square x is", square(x))

def square(n):
    # pangkat
    # return n ** n
    # pow
    return pow(n, 3)

main()

