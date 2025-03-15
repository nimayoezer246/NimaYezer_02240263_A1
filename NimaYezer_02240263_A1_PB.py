import random

def guess_number_game():
    min_num = 1
    max_num = 15
    secret_number = random.randint(min_num, max_num)
    max_attempts = 5
    attempts = 0
    
    print("\nWelcome to the Guess the Number game!")
    print(f"I'm thinking of a number between {min_num} and {max_num}. Can you guess it in {max_attempts} attempts?")
    
    while attempts < max_attempts:
        try:
            user_guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts!")
            return True  # User won
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
    
    print(f"\nSorry, you've used all {max_attempts} attempts. The correct number was {secret_number}.")
    return False  # User lost

def rock_paper_scissors():
    choices = ["Rock", "Paper", "Scissors"]
    user_score = 0
    computer_score = 0
    
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Choose one of the following options:")
    print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")
    
    while True:
        user_input = input("\nEnter your choice (1-3) or '4' to quit: ").strip()
        
        if user_input == "4":
            print("\nThanks for playing Rock, Paper, Scissors!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break
        
        if user_input not in ["1", "2", "3"]:
            print("Invalid option. Please choose 1, 2, 3, or 4.")
            continue
        
        user_choice = choices[int(user_input) - 1]
        computer_choice = random.choice(choices)
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            computer_score += 1
        
        print(f"Current Score - You: {user_score}, Computer: {computer_score}")

def game_selection():
    while True:
        print("\nHello, welcome to my game collection!")
        print("Please select a game to play:")
        print("1. Guess the Number\n2. Rock, Paper, Scissors\n3. Exit")
        
        try:
            game = int(input("Enter the number of your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if game == 1:
            print("\nYou have selected Guess the Number.")
            while True:
                guess_number_game()
                play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
                if play_again != "yes":
                    break
        
        elif game == 2:
            print("\nYou have selected Rock, Paper, Scissors.")
            rock_paper_scissors()
        
        elif game == 3:
            print("\nExiting the program. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    game_selection()