"""Practice while loops and debug them"""

my_number: int = 8675309
my_number_str: str = "8675309"
total: int = 0
index: int = 0
while index < len(my_number_str):
    value: int = int(my_number_str[index])
    total += value
    index += 1
