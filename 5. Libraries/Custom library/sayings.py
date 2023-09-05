def main():
    hello("World")
    goodbye("World")

def hello(name):
    print(f"Hello {name}")

def goodbye(name):
    print(f"Goodbye {name}")

# run code only if it run on this file instead of import
if __name__ == "__main__":
    main()