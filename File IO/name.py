# .append() to list
# sorted() mengurutkan list

# ================================
# WRITE FILE

# name = input("Name = ")

# "w" untuk write
# "a" untuk append
# "r" untuk read
# file.close()

#  Open file and write 
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# ==============================
# WRITE FILE

names = []

with open("File IO/names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print("Hello", name)




