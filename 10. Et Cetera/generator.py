def main():
    n = int(input("n = "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "Mbek" * i

main()