import random


names_list = input("Name list: ").split(", ")

print(f"{names_list[random.randint(0, len(names_list) - 1)]} is going to buy us dinner!!!!!")
