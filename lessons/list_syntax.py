"""Demonstrate Basic List Syntax."""

#Initialize an empty list
grocery_list: list[str] = list() # <- list constructor
grocery_list: list[str] = [] # literal

print(grocery_list)

# Add item to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print(grocery_list)

     
# Create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list:")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

#Indexing
print("Print first element of string")
print(grocery_list[0])

#Modifying by index
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change:")
print(grocery_list)

#Removing an item from a list
grocery_list.pop(1)
print("after removing almond milk:")
print(grocery_list)

#length of a list
len(grocery_list)

def display(x: list[str]):
    print(x)

display(grocery_list)
x = display(["Alyssa", "Erin", "AK"])
print(x)

def create(x: str, y: str) -> list[str]:
    cool_list: list[str] = [x, y]
    return cool_list

print(create("Ted", "Thavisin"))