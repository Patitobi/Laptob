import random as rand
class player:
    def __init__(self, name=None, id=int()):
        self.player_id = id
        name = input(f'Player{id+1} Name:')
        self.player_name = name
        self.cardes = list()

    def random_card(self):
        while True:
            rand_num = rand.randint(0, 7)
            work_card = game_cards[rand_num]
            if work_card[3] == 0:
                game_cards[rand_num][3] = 1
                return work_card


    def card_give(self):
        self.cardes = [(self.random_card()),
                       (self.random_card()),
                       (self.random_card())]
        self.show_cards()

    def show_cards(self):
        for x in self.cardes:
            print(x)
        

class game:
    def __init__(self, player=int()):
        self.player = player
        self.tabel_cards = list()
        self.player_ref = list()

        self.game_setup()

    def game_setup(self):
        for x in range(self.player):
            self.player_ref.append(player(name=None, id=x))
        self.give_cards()

    def give_cards(self):
        for x in self.player_ref:
            print(x)
            x.card_give()


# [(x , y, z)] x=tüp der carte y=bezeichung z=Wert in Zahlen
game_cards = [[0, 'A', 11, 0],
            [0, '7', 7, 0],
            [0, '8', 8, 0],
            [0, '9', 9, 0],
            [0, '10', 10, 0],
            [0, 'B', 10, 0],
            [0, 'D', 10, 0],
            [0, 'K', 10, 0]]
for y in range(4):
    for x in range(len(game_cards)):
        work_card = game_cards[x]
        work_card[0] = y+1
        work_cards = list()
        work_cards + (work_card)
game_cards=work_cards

if __name__ == '__main__':
    player_num = int(input('Anzal der spieler:'))
    spiel = game(player=player_num)
    print(game_cards)
