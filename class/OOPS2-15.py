'''15. Cricket Team Management
Problem

Create player management system.

Requirements

Each player:

name
role
runs scored
Functionalities
Update runs
Display statistics
Maintain total players
Additional Challenge

Find highest scorer among all players.'''


import random

class Player:
    def __init__(self, name, role, runs, num):
        self.__j_num = num
        self.__name = name
        self.__role = role
        self.__runs = runs

    def add_runs(self, runs):
        if runs < 0:
            print("Runs cannot be negative!")
            return

        self.__runs += runs

    def __str__(self):
        return (f"{self.__j_num} --> {self.__name} --> "
                f"{self.__role} --> {self.__runs} runs")

    def __lt__(self, other):
        return self.__runs < other.__runs


class CTM:
    def __init__(self):
        self.__jersey_numbers = set()
        self.__players = {}

    def add_player(self, name, role, runs):

        if any(key[1] == name for key in self.__players):
            print("Player already exists!")
            return

        j_num = random.randint(1, 1000)

        while j_num in self.__jersey_numbers:
            j_num = random.randint(1, 1000)

        self.__jersey_numbers.add(j_num)

        self.__players[(j_num, name)] = Player(
            name, role, runs, j_num
        )

        print(f"Player {name} added successfully!")
        print(f"Jersey Number: {j_num}")

    def update_runs(self, j_num, name, runs):

        key = (j_num, name)

        if key not in self.__players:
            print("Player not found!")
            return

        self.__players[key].add_runs(runs)
        print(f"Successfully updated runs of {name}")

    def highest_scorer(self):

        if not self.__players:
            print("No players available!")
            return

        players = list(self.__players.values())
        players.sort()

        print("\nHighest Scorer:")
        print(players[-1])

    def view_summary(self, j_num, name):

        key = (j_num, name)

        if key not in self.__players:
            print("Player not found!")
        else:
            print(self.__players[key])

    def view_all_players(self):

        if not self.__players:
            print("No players available!")
            return

        for player in self.__players.values():
            print(player)

    def total_players(self):
        print(f"Total Players: {len(self.__players)}")

    def get_jersey_number(self, name):
      for j_num, player_name in self.__players:
        if player_name == name:
            return j_num
      return None

    def update_runs(self, name, runs):

      j_num = self.get_jersey_number(name)
      
      if j_num is None:
        print("Player with given name and jersey number not found!")
        return
      
      key = (j_num, name)

      if key not in self.__players:
        print("Player with given name and jersey number not found!")
        return
        
      self.__players[key].add_runs(runs)

      print(f"Successfully updated runs of {name}!")
      print(f"Updated Statistics: {self.__players[key]}")


c = CTM()

c.add_player("Virat", "Batsman", 14000)
c.add_player("Rohit", "Batsman", 12342)
c.add_player("Shubhman", "Batsman", 8000)
c.add_player("KL Rahul", "Batsman", 10000)
c.add_player("Jadeja", "All-Rounder", 6000)
c.add_player("Hardik", "All-Rounder", 5600)
c.add_player("Axar", "All-Rounder", 3400)
c.add_player("Arshdeep", "Bowler", 1400)
c.add_player("Bumrah", "Bowler", 340)
c.add_player("Kuldeep", "Bowler", 140)
c.add_player("Bhuvneshwar", "Bowler", 520)
c.update_runs("Hardik", 100000)
c.view_all_players()
c.total_players()

c.highest_scorer()
