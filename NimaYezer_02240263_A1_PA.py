def is_prime_number(number):
    return number > 1 and all(number % divisor != 0 for divisor in range(2, int(number**0.5) + 1))

def calculate_prime_sum(start_num, end_num):
    try:
        start_num, end_num = int(start_num), int(end_num)
        prime_sum = sum(num for num in range(min(start_num, end_num), max(start_num, end_num) + 1) if is_prime_number(num))
        return f"Sum: {prime_sum}"
    except ValueError:
        return "Error: Invalid input"

def convert_length(length_value, length_unit):
    try:
        length_value = float(length_value)
        if length_unit.upper() == 'M':
            converted_value = round(length_value * 3.28084, 2)
            return f"{length_value} meter(s) = {converted_value} feet"
        else:
            converted_value = round(length_value / 3.28084, 2)
            return f"{length_value} foot/feet = {converted_value} meters"
    except ValueError:
        return "Error: Invalid input"

def count_consonants_in_text(input_text):
    consonant_count = sum(1 for char in input_text.lower() if char in 'bcdfghjklmnpqrstvwxyz')
    return f"Consonants: {consonant_count}"

def find_min_max(numbers_string):
    try:
        number_list = [float(num) for num in numbers_string.split()]
        return f"Min: {min(number_list)}, Max: {max(number_list)}"
    except ValueError:
        return "Error: Invalid input"

def check_if_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    return f"Is palindrome: {cleaned_string == cleaned_string[::-1]}"

def run_application():
    while True:
        print("\n1. Calculate Sum of Primes\n2. Convert Length\n3. Count Consonants")
        print("4. Find Min/Max Values\n5. Check Palindrome\n0. Exit")
        
        user_selection = input("\nSelect an option (0-5): ")
        
        if user_selection == '0':
            break
        elif user_selection == '1':
            print(calculate_prime_sum(input("Enter start number: "), input("Enter end number: ")))
        elif user_selection == '2':
            print(convert_length(input("Enter length value: "), input("Enter unit (M/F): ")))
        elif user_selection == '3':
            print(count_consonants_in_text(input("Enter text: ")))
        elif user_selection == '4':
            print(find_min_max(input("Enter numbers (space-separated): ")))
        elif user_selection == '5':
            print(check_if_palindrome(input("Enter text to check: ")))
        else:
            print("Invalid choice")
            
        if input("\nContinue? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    run_application()