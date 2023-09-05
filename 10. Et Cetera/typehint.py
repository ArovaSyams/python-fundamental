
# -> str is define the return value
def meow(n: int) -> str:
    return "Meow\n" * n

number: int = int(input("n: "))
meow: str = meow(3)
print(meow, end="")