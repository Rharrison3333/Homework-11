import random


def roll_die():
    sides = ["L", "C", "R", ".", ".", "."]
    return random.choice(sides)


def active_players(chips):
    count = 0

    for chip_count in chips:
        if chip_count > 0:
            count += 1

    return count


def show_chips(chips, center):
    print("Current chips:")

    for i in range(len(chips)):
        print("Player", i + 1, ":", chips[i])

    print("Center pot:", center)
    print()


def main():
    players = int(input("Enter number of players: "))

    while players < 3:
        print("LCR needs at least 3 players.")
        players = int(input("Enter number of players: "))

    chips = [3] * players
    center = 0
    turn = 0
    round_number = 1

    while active_players(chips) > 1:
        print("Round", round_number)

        for i in range(players):
            turn = i

            if active_players(chips) == 1:
                break

            print("Player", turn + 1, "turn")

            dice_to_roll = chips[turn]

            if dice_to_roll > 3:
                dice_to_roll = 3

            if dice_to_roll == 0:
                print("Player", turn + 1, "has no chips and skips.")
            else:
                rolls = []

                for d in range(dice_to_roll):
                    rolls.append(roll_die())

                print("Rolls:", rolls)

                for roll in rolls:
                    if roll == "L":
                        left = (turn - 1) % players
                        chips[turn] -= 1
                        chips[left] += 1
                    elif roll == "R":
                        right = (turn + 1) % players
                        chips[turn] -= 1
                        chips[right] += 1
                    elif roll == "C":
                        chips[turn] -= 1
                        center += 1

            show_chips(chips, center)

        round_number += 1

    for i in range(players):
        if chips[i] > 0:
            winner = i

    chips[winner] += center

    print("Player", winner + 1, "wins!")
    print("They receive the center pot.")
    print("Final chips:", chips)


main()
