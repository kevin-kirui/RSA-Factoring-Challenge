#!/usr/bin/python3
import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorize_and_print(num):
    print("{:d}=".format(num), end="")
    if num % 2 == 0:
        print("{}*2".format(num//2))
        return

    for i in range(3, num, 2):
        if num % i == 0 and is_prime(i):
            factor = num // i
            if is_prime(factor):
                print("{}*{}".format(factor, i))
                return

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path) as f:
            for line in f:
                num = int(line)
                factorize_and_print(num)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
