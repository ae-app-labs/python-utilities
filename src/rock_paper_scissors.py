import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player_choice, computer_choice):
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if player_choice == computer_choice:
        return "It's a tie!"
    elif winning_combinations[player_choice] == computer_choice:
        return 'You win!'
    else:
        return 'Compueter Wins!'
    

def play_game():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice!")
        return
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = get_winner(player_choice, computer_choice)
    print(result)


# Play the game
play_game()
