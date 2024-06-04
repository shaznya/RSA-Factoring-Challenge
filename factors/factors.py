#!/usr/bin/python3
import sys

def factorize(num):
    factors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append((i, num // i))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        numbers = file.read().splitlines()

    try:
        for number in numbers:
            num = int(number)
            factor_pairs = factorize(num)
            for pair in factor_pairs:
                print(f"{num}={pair[0]}*{pair[1]}")
    except KeyboardInterrupt:
        pass

    file.close()

if __name__ == "__main__":
    main()
