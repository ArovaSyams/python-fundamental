# WHILE
# i = 0
# while i < 3:
#     print("Meow")
#     i += 1

# FOR
# for _ in range(3):
#     print("meow")

# =============

# while True:
#     n = int(input("n = "))
#     if n > 0:
#         break
    # if n < 0:
    #     continue
    # else
    #     break

# for _ in range(n):
#     print("meow")

# ==============

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("n = "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
