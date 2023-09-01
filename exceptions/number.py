# try except
# try:
#     x = int(input("x = "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not integer")

# try except else
# try:
#     x = int(input("x = "))
# except ValueError:
#     print("x is not integer")
# else:
#     print(f"x is {x}")


# while try except
# while True:
#     try:
#         x = int(input("x = "))
#     except ValueError:
#         print("x is not integer")
#     else:
#         break
# print(f"x is {x}")


# try except with function
def main():
    x = get_int("x = ")
    print(f"x is {x}")

def get_int(prompt):
    # while True:
    #     try:
    #         x = int(input("x = "))
    #     except ValueError:
    #         print("x is not integer")
    #     else:
    #         return x
    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # pass = tetap ada tapi di ignore
            pass

main()
