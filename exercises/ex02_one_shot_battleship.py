"""EX02 - One Shot Battleship"""

__author__ = "730676554"

size: int = 4
secret_row: int = 3
secret_column: int = 2

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""

row_guess: int = int(input("Guess a row: "))
while row_guess > size:
    row_guess = int(input(f'The grid is only {size} by {size}. Try again: '))
    
column_guess: int = int(input("Guess a column: "))
while column_guess > size:
    column_guess = int(input(f'The grid is only {size} by {size}. Try again: '))

if column_guess == secret_column and row_guess == secret_row:
    result = RED_BOX
else:
    result = WHITE_BOX

row_counter: int = 1
while row_counter <= size:
    row_emojis: str = ""
    column_counter: int = 1
    if row_guess == row_counter:
        while column_counter <= size:
            if column_guess == column_counter:
                row_emojis = row_emojis + result
            else:
                row_emojis = row_emojis + BLUE_BOX
            column_counter = column_counter + 1
    else:
        while column_counter <= size:
            row_emojis = row_emojis + BLUE_BOX
            column_counter = column_counter + 1
    print(row_emojis)
    row_counter = row_counter + 1

if column_guess == secret_column and row_guess == secret_row:
    print("Hit!")
elif column_guess == secret_column:
    print("Close! Correct column, wrong row.")
elif row_guess == secret_row:
    print("Close! Correct row, wrong column.")
else:
    print("Miss!")
