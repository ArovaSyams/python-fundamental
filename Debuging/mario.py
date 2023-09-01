def main():
    height = int(input("x = "))
    pyramid(height)

def pyramid(h):
    for i in range(h):
        print("#" * (i + 1))

main()