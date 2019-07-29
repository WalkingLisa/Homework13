#coding=utf8

from sport_class import Player
from sport_class import FootballPlayer
from sport_class import BasketballPlayer

if __name__ == '__main__':

    print("Create your own player!")


    while True:
        choice=input("Which player do you want to create? Basketball or Football?: ")
        if choice=="Football":
            f_name = input("Enter player's first name: ")
            l_name = input("Enter player's last name: ")
            height = input("Enter player's height: ")
            weight = input("Enter player's weight: ")
            goals = input("Enter the number of player's goals: ")
            y_cards = input("Enter the number of player's yellow cards: ")
            r_cards = input("Enter the number of player's red cards: ")
            new_player_foot = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),goals=int(goals), yellow_cards=int(y_cards), red_cards=int(r_cards))
            try:
                with open("football_players.txt", "w") as football_file:
                    football_file.write(str(new_player_foot.__dict__))
                print("Player successfully entered!")
                print("Player's data: {0}".format(new_player_foot.__dict__))
            except:
                raise FileNotFoundError



        elif choice=="Basketball":
            f_name = input("Enter player's first name: ")
            l_name = input("Enter player's last name: ")
            height = input("Enter player's height: ")
            weight = input("Enter player's weight: ")
            points = input("Enter player's points: ")
            rebounds = input("Enter player's rebounds: ")
            assists = input("Enter player's assists: ")
            new_player_basket = BasketballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight), points=int(points), assists=int(assists), rebounds=int(rebounds))
            try:
                with open("basketball_players.txt", "w") as basketball_file:
                    basketball_file.write(str(new_player_basket.__dict__))
                print("Player successfully entered!")
                print("Player's data: {0}".format(new_player_basket.__dict__))
            except:
                raise FileNotFoundError



