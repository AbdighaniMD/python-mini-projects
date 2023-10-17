import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

#print(roll())

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players. ")
    else:
        print("Invalid input, try again please.")

#print(players)

max_score = 5
players_score = [0 for _ in range(players)]
#print(players_score)

while max(players_score) < max_score:

    for player_index in range(players):

        print("\nPlayer number", player_index + 1, "Your turn has just started!\n")
        print("Your total score is:", players_score[player_index], "\n")
        
        current_Score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("You have rolled 1! Turn done")
                #current_Score = 0
                break
            else:
                current_Score += value
                print("You have rolled a: ", value)

            print("Your score is: ", current_Score)

        players_score[player_index] += current_Score
        print("Your total score is:", players_score[player_index])

print(" ")
max_score = max(players_score)
winning_index = players_score.index(max_score)
print("Player number", winning_index + 1,
      "is the winner with a score of:", max_score)
