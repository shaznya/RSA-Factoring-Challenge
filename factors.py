import sys
import time

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

    try:
        with open(input_file, 'r') as file:
            numbers = file.read().splitlines()

        for number in numbers:
            num = int(number)
            factor_pairs = factorize(num)
            for pair in factor_pairs:
                print(f"{num}={pair[0]}*{pair[1]}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except ValueError:
        print(f"Invalid input in '{input_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f} seconds.")
