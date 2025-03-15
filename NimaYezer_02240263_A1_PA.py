import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum(start, end):
    """Calculate the sum of all prime numbers within a range."""
    return sum(n for n in range(start, end + 1) if is_prime(n))

def length_converter(value, unit):
    """Convert between meters and feet."""
    if unit.upper() == 'M':
        return round(value * 3.28084, 2)  # Meters to Feet
    elif unit.upper() == 'F':
        return round(value / 3.28084, 2)  # Feet to Meters
    else:
        raise ValueError("Invalid conversion unit. Use 'M' or 'F'.")

def count_consonants(text):
    """Count the number of consonants in a string."""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in text if char in consonants)

def min_max_finder(numbers):
    """Find the smallest and largest numbers in a list."""
    return min(numbers), max(numbers)

def is_palindrome(text):
    """Check if a string is a palindrome, ignoring spaces and case."""
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]

def word_counter(file_path):
    """Count occurrences of specified words in a file."""
    target_words = ["the", "was", "and"]
    word_count = {word: 0 for word in target_words}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().lower().split()
        for word in target_words:
            word_count[word] = words.count(word)
    
    return word_count

def main():
    while True:
        print("\nSelect a function (1-6):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in a string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("7. Exit program")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                print("Sum of prime numbers:", prime_sum(start, end))
            except ValueError:
                print("Invalid input. Please enter integers.")
        
        elif choice == '2':
            try:
                value = float(input("Enter length value: "))
                unit = input("Convert to (M for meters, F for feet): ")
                print("Converted value:", length_converter(value, unit))
            except ValueError:
                print("Invalid input. Please enter a number and a valid unit.")
        
        elif choice == '3':
            text = input("Enter a string: ")
            print("Number of consonants:", count_consonants(text))
        
        elif choice == '4':
            try:
                num_count = int(input("How many numbers will you enter? "))
                numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num_count)]
                min_val, max_val = min_max_finder(numbers)
                print(f"Smallest: {min_val}, Largest: {max_val}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        
        elif choice == '5':
            text = input("Enter a string: ")
            print("Is palindrome:", is_palindrome(text))
        
        elif choice == '6':
            file_path = input("Enter the path to the text file: ")
            try:
                print("Word counts:", word_counter(file_path))
            except FileNotFoundError:
                print("File not found. Please enter a valid file path.")
        
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
        
        again = input("Would you like to try another function? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
