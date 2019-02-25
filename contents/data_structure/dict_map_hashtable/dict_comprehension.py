#!/bin/python3

# Program to create a dictionary using dictionary comprehensin.

houses = [
    "House Stark",
    "House Baratheon",
    "House Lanister",
    "House Tully",
    "House Arryn",
    "House Tyrell",
    "House Martell", ]

lords = [
    "Ned Stark",
    "Robert Baratheon",
    "Tywin Lanister",
    "Admure Tully",
    "John Arryn",
    "Mace Tyrell",
    "Doran Martell", ]

westeros_dict = {houses[i]: lords[i] for i in range(7)}

for house, lord in westeros_dict.items():
    print(house + ": " + lord)
