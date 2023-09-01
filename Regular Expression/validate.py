import re

email = input("your email = ")

# r"" for raw
# . = any char
# + = pengulangan mulai dari 1
# * = pengulangan mulai dari 0
# ^ = match start of string
# $ = match end of string
# [^@] = semua char kecuali @
# [a-zA-Z0-9] = include all set writed
# \w = all letter, numbers, underscores
if re.search(r"^\w+@\w+\.(com|edu|gov)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")