def main():
    yell("This", "is", "me!")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

main()