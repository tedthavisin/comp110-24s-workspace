"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730676554"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

result: str = ""
boats: str = ""
boat_location: int = 2

player1_number: int = int(input("Pick a secret boat location between 1 and 4: "))
if player1_number > 4:
    print("Error!", player1_number, "too high!")
    exit()
if player1_number < 1:
    print("Error!", player1_number, "too low!")
    exit()

player2_number: int = int(input("Guess a number between 1 and 4: "))
if player2_number > 4:
    print("Error!", player2_number, "too high!")
    exit()
if player2_number < 1:
    print("Error!", player2_number, "too low!")
    exit()


if (player2_number == player1_number):
    result = RED_BOX
else:
    result = WHITE_BOX

if player2_number == 1:
    boats = boats + result
else:
    boats = boats + BLUE_BOX

if player2_number == 2:
    boats = boats + result
else:
    boats = boats + BLUE_BOX

if player2_number == 3:
    boats = boats + result
else:
    boats = boats + BLUE_BOX

if player2_number == 4:
    boats = boats + result
else:
    boats = boats + BLUE_BOX

print(boats)
if (player1_number == player2_number):  
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")