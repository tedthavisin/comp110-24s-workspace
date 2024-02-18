"""Functional Battleship."""

__author__ = "730676554"

import random

def input_guess(size: int, type: str) -> int:
    assert type == "row" or type == "column"
    guess: int = int(input(f'Guess a {type}: '))
    while guess < 1 or guess > size:
        guess: int = int(input(f'The grid is only {size} by {size}. Try again: '))
    return guess


def print_grid(size: int, row_guess: int, column_guess: int, user_guess: bool) -> None:

    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result: int = ""

    if user_guess == True:
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


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False
    
def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    row: int = secret_row
    column: int = secret_column
    size: int = grid_size
    user_row_guess: int = 0
    user_column_guess: int = 0
    turn_counter: int = 1
    win: bool = False
    
    while turn_counter <= 5 and win == False:
        print(f'=== Turn {turn_counter}/5 ===')
        user_row_guess = input_guess(size, "row")
        user_column_guess = input_guess(size, "column")
        user: bool = correct_guess(row, column, user_row_guess, user_column_guess)
        print_grid(size, user_row_guess, user_column_guess, user)
        if user == True:
            print("Hit!")
            print(f'You won in {turn_counter}/5 turns!')
            win = True
        else:
            print("Miss!")
        turn_counter = turn_counter + 1
        if turn_counter == 6:
            print("X/5 - Better luck next time!")

if __name__ == "__main__":
        grid_size: int = random.randint(3, 5)
        main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))