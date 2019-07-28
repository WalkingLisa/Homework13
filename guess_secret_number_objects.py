import datetime
import json
import random


class Player():
    def __init__(self, player_name): #, score, date):
        self.player_name = player_name
       # self.score=score
      #  self.date=date

print("Welcome to this wonderful game!")

p_name = input("Enter your name to start the game: ")

new_player = Player(player_name=p_name)

with open("results.txt", "w") as result_file:
    result_file.write(str(new_player.__dict__))

print("Player successfully entered!")
print("{0}".format(new_player.__dict__))

# Function for playing the game
def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("scoreboard.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")


# Get a list of all scores
def get_score_list():
    with open("scoreboard.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


# Return top 3 scores
def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list


# Run the game
while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break