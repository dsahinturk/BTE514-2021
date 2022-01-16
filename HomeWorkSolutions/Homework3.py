import random


def dice_roller():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2

    while dice1 == dice2:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum += (dice1 + dice2)

    return sum


def calculate_interest_goal(P0, i, goal):
    if P0 < 0:
        return 0

    count = 0
    while P0 < goal:
        P0 = P0 * (1 + i)
        count += 1

    return count


def test_dice_roller():
    print("******************* Soru 1 cozum ******************")
    print("Sum:", dice_roller())
    print("******************* Soru 1 cozum ******************\n")


def test_i_goal():
    print("******************* Soru 2 cozum ******************")
    print("Steps:", calculate_interest_goal(1000, 0.05, 2000))
    print("******************* Soru 2 cozum ******************\n")
