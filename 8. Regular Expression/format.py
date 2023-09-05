import re

name = input("Name = ")


# := = walrus operator (untuk mereturn boolean)
if matches := re.search("^(.+), *(.+)$", name):

    name = matches.group(2) + " " + matches.group(1)

print(f"Hello {name}")
