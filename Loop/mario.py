def main():
    print_square(10, 8)

def print_square(height, width):
    for i in range(height):
        for j in range(width):
            print("#", end="")
        print()

main()