#!/usr/bin/python3
import sys

def factorize(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None

def main(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            n = int(line.strip())
            factors = factorize(n)
            if factors:
                print(f"{n}={factors[0]}*{factors[1]}")
            else:
                print(f"{n} is a prime number")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
