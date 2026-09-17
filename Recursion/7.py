"""3.
Cricket Tournament – Highest Run Scorer

A cricket academy wants to reward the player who scored the highest number of runs in a tournament.

Write a Python program to identify the highest run scorer using reduce() and a lambda expression.

Input
players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]
Expected Output
Highest Run Scorer: Rohit"""
from functools import reduce
players =int(input("Enter number of players:"))
players = []
for i in range(players):
    name = input("Enter player name: ")
    runs = int(input("Enter runs scored: "))
    players.append((name, runs))
highest_scorer = reduce(lambda x, y: x if x[1] > y[1] else y, players)
print(f"Highest Run Scorer: {highest_scorer[0]}")