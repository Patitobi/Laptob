import random as rand

class player:
    def __init__(self, id=int()):
        self.player_id = id
        name = input(f'Player{id+1} Name:')
        self.player_name = name
        self.cardes = list()

    def card_give(self):
        self.cardes = [(random_card()),
                       (random_card()),
                       (random_card())]
        self.show_cards()

    def show_cards(self):
        print(self.player_name)
        print(self.cardes)        

class game:
    def __init__(self, player=int()):
        self.player = player
        self.tabel_cards = list()
        self.player_ref = list()

        self.game_setup()

    def game_setup(self):
        for x in range(self.player):
            self.player_ref.append(player(id=x))
        self.give_cards()

    def give_cards(self):
        for x in self.player_ref:
            x.card_give()

    def tabel_cards_give(self):
        self.tabel_cards = [(random_card()),
                            (random_card()),
                            (random_card())]

def random_card():
    while True:
        rand_num = rand.randint(0, len(game_cards))
        work_card = game_cards[rand_num]
        if work_card[3] == 0:
            game_cards[rand_num][3] = 1
            return work_card

#ertellen der spielcarten durch un umgängliche festlegunen und dann vervielfeltigung
#gamecard[0][0] = typ
#gamecard[0][1] = bezeichnung
#gamecard[0][2] = wert
#gamecard[0][3] = vergebben(1) oder nicht(0)
cards_name = ['7', '8', '9', '10', 'B', 'D', 'K', 'A']
cards_val = [7,8,9,10,10,10,10,11]
game_cards = list()
for x in range(4):
    for y in range(len(cards_name)):
        work_cards = [x, cards_name[y], cards_val[y], 0]
        game_cards.append(work_cards)

#spielstart
if __name__ == '__main__':
    player_num = int(input('Anzal der spieler:'))
    spiel = game(player=player_num)
