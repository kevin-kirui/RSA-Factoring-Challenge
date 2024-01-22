#!/usr/bin/python3
import math
import sys

def factorize_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            p, q = factorize_number(number)
            if p is not None and q is not None:
                print(f"{number}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize_file(file_path)

