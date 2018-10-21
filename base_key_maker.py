import random
characters = list(input("Enter all the characters: "))
print(characters)
random.shuffle(characters)
print("".join(characters))
