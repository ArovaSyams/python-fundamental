import argparse

parser = argparse.ArgumentParser(description="Meow adalah kucing")
parser.add_argument("-n", type=int, default=1, help="n is count of meow")
args = parser.parse_args()

for _ in range(args.n):
    print("Meow")