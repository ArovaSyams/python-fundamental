# docstring is a method to explain the code that than can be readed and convert to usefull PDF, Web Page etc.
# with """.."""

def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of time in meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: A String of n meows, one per line
    :rtype: str
    """
    return "Meow\n" * n

number: int = int(input("n: "))
meow: str = meow(3)
print(meow, end="")