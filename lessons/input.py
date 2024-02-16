"""PRACTICE WITH USER INPUT"""


name: str = (input("What is your name?"))
number: int = 1
print("Hello " + name + "!")

def mimic(my_words: str) -> str:
    """Given the str my_words, outputs the same string."""
    return my_words