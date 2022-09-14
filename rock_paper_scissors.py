import random

def get_choices():
    player_choice = input("Enter your choices (rock, paper, scissors) :")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player ,computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes Scissors! You Win!"
    else:
      return "Paper covers rock...You lose hehe"
  elif player == "paper":
    if computer == "rock":
      return "Rock covers paper!...You Win!"
    else:
      return "Scissors cut paper...You lose hehe"
  elif player == "scissors":
    if computer == "rock":
      return "Rock smashes scissors...You lose hehe"
    else:
      return "Scissors cut paper! You win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

      
