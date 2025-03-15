def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def sum_of_primes(start, end):
    try:
        start, end = int(start), int(end)
        return f"Sum: {sum(n for n in range(min(start,end), max(start,end) + 1) if is_prime(n))}"
    except ValueError:
        return "Error: Invalid input"

def length_converter(value, unit):
    try:
        value = float(value)
        return f"{value} {unit}s = {round(value * 3.28084 if unit.upper()=='M' else value/3.28084, 2)} {'feet' if unit.upper()=='M' else 'meters'}"
    except ValueError:
        return "Error: Invalid input"

def count_consonants(text):
    return f"Consonants: {sum(1 for c in text.lower() if c in 'bcdfghjklmnpqrstvwxyz')}"

def min_max_finder(numbers):
    try:
        nums = [float(x) for x in numbers.split()]
        return f"Min: {min(nums)}, Max: {max(nums)}"
    except ValueError:
        return "Error: Invalid input"

def palindrome_checker(text):
    clean = ''.join(c.lower() for c in text if c.isalnum())
    return f"Is palindrome: {clean == clean[::-1]}"

def main():
    while True:
        print("\n1. Sum of Primes\n2. Length Converter\n3. Count Consonants")
        print("4. Min/Max Finder\n5. Palindrome Check\n0. Exit")
        
        choice = input("\nChoice (0-5): ")
        
        if choice == '0':
            break
        elif choice == '1':
            print(sum_of_primes(input("Start: "), input("End: ")))
        elif choice == '2':
            print(length_converter(input("Value: "), input("Unit (M/F): ")))
        elif choice == '3':
            print(count_consonants(input("Text: ")))
        elif choice == '4':
            print(min_max_finder(input("Numbers (space-separated): ")))
        elif choice == '5':
            print(palindrome_checker(input("Text: ")))
        else:
            print("Invalid choice")
            
        if input("\nContinue? (y/n): ").lower() != 'y':
            break

if _name_ == "_main_":
    main()