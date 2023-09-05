def main():
    x = int(input("X = "))
    
    if is_even(x):
        print("is even")
    else:
        print("is odd")

def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    # pythonic
    # return True if n % 2 == 0 else False

    return n % 2 == 0
    
main()