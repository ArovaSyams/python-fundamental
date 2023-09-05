# get the spesific function
# from random import choice

import random

# make random probability
# coin = random.choice(["Gunting", "Batu", "Kertas"])

# make random probability between 1 - 10
# number = random.randint(1, 10)

# make random order on a list
cards = ['jack', 'queen', 'king']

random.shuffle(cards)

for card in cards:
    print(card)