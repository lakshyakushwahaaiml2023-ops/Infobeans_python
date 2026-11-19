'''15. Sports Management
Player
CricketPlayer
Captain(CricketPlayer)

Add captain-specific functionality.'''

class Player:
    def __init__(self, name, j_num):
        self.__name = name
        self.__j_num = j_num

    def __str__(self):
        return f"{self.__name} | {self.__j_num}"

class CricketPlayer(Player):
    def __init__(self, name, j_num, team, role):
        super().__init__(name, j_num)
        self.__team = team
        self.__role = role

    def __str__(self):
        return f"{super().__str__()} | {self.__team} | {self.__role}"

class Captain(CricketPlayer):
    def __init__(self, name, j_num, team, role, capt_since, match_won):
        super().__init__(name, j_num, team, role)
        self.__capt_since = capt_since
        self.__match_won = match_won

p = Player("Dhoni", 7)
print(p)

cp = CricketPlayer("Dhoni", 7, "India", "Wicket Keeper")
print(cp)

c = Captain("Dhoni", 7, "India", "Wicket Keeper")
print(c)