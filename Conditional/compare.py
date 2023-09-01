x = int(input("x = "))
y = int(input("y = "))

if x > y:
    print("x > y")
if x < y:
    print("y > x")
if x == y:
    print("x = y")

# else if
if x > y:
    print("x > y")
elif x < y:
    print("y > x")
elif x == y:
    print("x = y")

# or
if x > y or x < y:
    print("x is not equal")
else:
    print("x is equal")