import random


def roll_dice(number):
    dice = []

    for i in range(number):
        dice.append(random.randint(1, 6))

    return dice


def take_turn(player):
    print()
    print("Player", player, "turn")

    needed = 6
    saved = []
    cargo = []
    dice_left = 5
    score = 0

    for roll_number in range(1, 4):
        input("Press Enter to roll.")

        roll = roll_dice(dice_left)
        print("Roll", roll_number, ":", roll)

        if needed in roll:
            saved.append(needed)
            roll.remove(needed)

            if needed == 6:
                print("Ship found.")
                needed = 5
            elif needed == 5:
                print("Captain found.")
                needed = 4
            elif needed == 4:
                print("Crew found.")
                needed = 0

            dice_left -= 1

        if needed == 0:
            cargo = roll
            score = sum(cargo)
            print("Cargo dice:", cargo)
            print("Current score:", score)
            dice_left = 2

    if needed != 0:
        score = 0

    print("Player", player, "score:", score)
    return score


def play_game(players):
    scores = []

    for player in range(1, players + 1):
        score = take_turn(player)
        scores.append(score)

    high_score = max(scores)

    winners = []

    for i in range(len(scores)):
        if scores[i] == high_score:
            winners.append(i + 1)

    while len(winners) > 1:
        print()
        print("Tie between players:", winners)
        new_scores = []

        for player in winners:
            score = take_turn(player)
            new_scores.append(score)

        high_score = max(new_scores)
        new_winners = []

        for i in range(len(new_scores)):
            if new_scores[i] == high_score:
                new_winners.append(winners[i])

        winners = new_winners

    print()
    print("Player", winners[0], "wins!")


def main():
    players = int(input("Enter number of players: "))

    while players < 2:
        print("This game needs at least 2 players.")
        players = int(input("Enter number of players: "))

    play_game(players)


main()
