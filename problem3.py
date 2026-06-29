import random


def roll_three():
    return [
        random.randint(1, 6),
        random.randint(1, 6),
        random.randint(1, 6)
    ]


def take_turn(player, round_number):
    score = 0

    print()
    print("Player", player, "- Round", round_number)

    while True:
        input("Press Enter to roll.")

        dice = roll_three()

        print("Roll:", dice)

        if dice[0] == round_number and dice[1] == round_number and dice[2] == round_number:
            print("BUNCO!")
            score += 21
            print("Score:", score)
            continue

        elif dice[0] == dice[1] == dice[2]:
            print("Mini Bunco!")
            score += 5
            print("Score:", score)
            continue

        points = 0

        for die in dice:
            if die == round_number:
                points += 1

        if points == 0:
            break

        score += points
        print("Points earned:", points)
        print("Current score:", score)

    print("Turn over. Total score:", score)
    return score


def main():
    players = 4
    scores = [0, 0, 0, 0]

    sets = int(input("Enter number of sets (2-4): "))

    while sets < 2 or sets > 4:
        sets = int(input("Enter 2, 3, or 4 sets: "))

    for game_set in range(1, sets + 1):
        print()
        print("===== Set", game_set, "=====")

        for round_number in range(1, 7):
            print()
            print("----- Round", round_number, "-----")

            for player in range(players):
                scores[player] += take_turn(player + 1, round_number)

    print()
    print("Final Scores")

    for i in range(players):
        print("Player", i + 1, ":", scores[i])

    winner = scores.index(max(scores))

    print()
    print("Player", winner + 1, "wins!")


main()
