import time
import random

Troll = []      # score of troll
Player = []     # score of player
items = []      # player collects his items
attempts = []   # tracking if player went to the\n same place more than twice
turns_game = 3  # turns of die game with the troll
index = 0


def print_pause(message):
    print(message)
    time.sleep(1)


def winning_message():
    print_pause("The spell has been undone and you can go back home!")
    print_pause("You won!")
    play_again()


def losing_message():
    print_pause("GAME OVER!")
    print_pause("You can't kill the troll without a sword.")
    play_again()


def message_sword():
    print_pause("Luckily you have the Crystal Sword!\n"
                "You kill the troll")
    print_pause("Cangratulations, the spell has been undone")
    play_again()


def intro():
    print_pause("Last night you played cards with a stranger\n"
                "in a shady bar down the rode.")
    print_pause("You played with marked cards.")
    print_pause("Your opponent found out\nthat you have been cheating")
    print_pause("It turned out the stranger\n"
                "is actually an old troll\n"
                "called Uazu living in the Forgotten Forest")
    print_pause("He put a spell on you\n"
                "and you turned into ugly, smelly ogre.")
    print_pause("You have to find a way to break the spell.")


def valid_answer(valid, answer):
    if valid in answer:
        print_pause(f"Correct! It's {valid}!")
        print_pause("Because you are a man of a bright mind\n"
                    "you can get a Crystal Sword.")
        print_pause("Use it wisely. Be well!")
        items.append("crystal sword")
    else:
        print_pause("That's not correct answer.\n"
                    f"It's {valid} Go away!\n"
                    "You are not smart enough for Crystal Sword!")


def riddle_1():
    valid = "darkness"
    print_pause("The more of this there is, the less you see. What is it?")
    answer = input("Type your answer\n").lower()
    valid_answer(valid, answer)


def riddle_2():
    valid = "table"
    print_pause("What has legs, but doesn’t walk?")
    answer = input("Type your answer\n").lower()
    valid_answer(valid, answer)


def die_roll():
    return(random.randint(1, 6))


def die_game():
    index = 0
    while index < turns_game:
        print_pause(f"ROUND {index + 1}")
        print_pause("Troll rolls the die:")
        score1 = die_roll()
        print_pause("Troll gets " + str(score1))
        Troll.append(score1)
        print_pause("Your turn")
        print_pause("You roll the die:")
        score2 = die_roll()
        print_pause("You get " + str(score2))
        Player.append(score2)
        time.sleep(2)
        index += 1
        if score1 > score2:  # score in each turn
            print_pause("Troll wins this round!")
        elif score1 == score2:
            print_pause("Tie!")
        else:
            print("You won this round!")
    print_pause(winner())


def winner():
    if sum(Troll) == sum(Player):
        print("It is a tie! Once again!")
        die_game()
    elif sum(Troll) < sum(Player):
        return("You won the dice game!!")
    else:
        return("You lose the dice game!")


def friend():
    if "f1" in attempts:
        print_pause("Are you drunk?")
    elif "die" in items:
        print_pause("I'm sorry I can't help you anymore.")
        attempts.append("f1")
    else:
        print_pause("You approched Margaux.\n"
                    "She heard already about last night.")
        print_pause("She told you, you might ask an old man,\n"
                    "who is leaving in the Magic Cave,\n"
                    "if he can break this spell.")
        print_pause("Before you left, she gave you a die.")
        items.append("die")
    go_to()


def cave():
    if "c2" in attempts:
        print_pause("Go away! I'm tired!")
    elif "crystal sword" in items:
        print_pause("You got your magic sword,\n"
                    "now go to Forgotten Forest to beat the troll!")
        attempts.append("c2")
    else:
        print_pause("You meet an old man in Magic Cave.")
        print_pause("He said, you must kill the troll,\n"
                    "but you have to get a Crystal Sword")
        print_pause("I can give you the Sword, but only under one condition:")
        print_pause("you need to answer on my riddle!")
        decision = input("Do you want to try? yes/no?\n").lower()
        if decision == "no":
            print_pause("You left the cave without sword")
        elif decision == "yes":
            riddles = [riddle_1, riddle_2]
            riddle = random.choice(riddles)()
            return(riddle)
        else:
            print_pause("invalid input. Try again")
    go_to()


def forgotten_forest(items):
    print_pause("You've arrived to Forgotten Forest")
    print_pause("Uazu the troll approached you")
    print_pause("Uazu: Well, well, well... who decided to disturb my peace?")
    print_pause("It is you! You con man! You tried to cheat.I will kill you!")
    if "die" in items:
        print_pause("Oh! Die! I love this game!\n"
                    "Do you want a play? If you win I will undo the spell!\n"
                    "If you loose you will be an ogre to the end of your life")
        while True:
            reply = input("Do you want to play a game? Yes/No\n").lower()
            if reply == "yes":
                die_game()
                if sum(Troll) > sum(Player):
                    if "crystal sword" in items:
                        print_pause("In dice game there was no luck for you,\n"
                                    "but you still have your Crystal Sword.\n"
                                    "You are killing the troll.")
                        print_pause("You won")
                    else:
                        losing_message()
                else:
                    winning_message()
            elif reply == "no":
                print_pause("Troll attacks you!")
                if "crystal sword" in items:
                    message_sword()
                else:
                    losing_message()
            else:
                print("Invalid input.")
    elif "crystal sword" in items:
        message_sword()
    else:
        print_pause("You have been defeated by the troll. You lost")
    play_again()


def go_to():
    choice = input("Where you want to go?\n"
                   "Enter 1 to go to your best friend Margaux\n"
                   "Enter 2 to go to Magic Cave\n"
                   "Enter 3 to go to Forgotten Forest\n").lower()
    if "1" in choice:
        friend()
    elif "2" in choice:
        cave()
    elif "3" in choice:
        forgotten_forest(items)
    else:
        print("Something went wrong. Select 1, 2 or 3")
    go_to()


def play_again():
    print_pause("Do you want to start again?")
    response = input("Enter yes or no\n").lower()
    while True:
        if "yes" in response:
            print_pause("Starting the game")
            items.clear()
            attempts.clear()
            play_game()
        elif "no" in response:
            print_pause("Be well and don't cheat again!")
            exit()
        else:
            print("Invalid input")
        play_again()


def play_game():
    intro()
    go_to()
    play_again()


play_game()
