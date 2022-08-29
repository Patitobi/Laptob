import random as rand

class player_ob:
    def __init__(self, id=int(), game_ref=object()):
        self.player_id = id
        name = input(f'Player{id+1} Name:')
        self.player_name = name
        self.cardes = list()
        self.total_val = int()
        self.tabel_id = game_ref
        
    def card_give(self):
        self.cardes = [(random_card()),
                       (random_card()),
                       (random_card())]
        self.show_cards_player()

    def show_cards_dev(self):
        print(self.player_name)
        print(self.cardes)
    
    def show_cards_player(self):
        print(self.player_name)
        for x in range(len(self.cardes)):
            print(self.cardes[x][0], self.cardes[x][1])
            
    def player_turn(self):
        player_in = None
        while player_in == None:
            print(chr(27) + "[2J")
            self.tabel_id.show_tabel_cards()
            self.show_cards_player()
            print(self.player_name)
            print('Switch/Close/Pass:')
            player_in = input()
            player_in = self.player_in_check(player_in)
            if player_in == 'Switch':
                return self.card_switch()
            elif player_in == 'Close':
                return 'close'
            elif player_in == 'Pass':
                return 'pass'
            
    def player_in_check(self, player_input):
        # diconary machen mir alle möglichkeiten und abfragen return ist ein True or False
        if player_input == '' or None:
            return None
        elif len(player_input) < 3:
            return None
        elif player_input == 'Switch':
            return 'Switch'
        elif player_input == 'Close':
            return'Close'
        elif player_input == 'Pass':
            return 'Pass'
        else:
            return None
        
    def card_switch_all(self):
        pass   
    
    def card_switch(self):
        print('Tabel Card(1-3/all):')
        tabel_card_swap = input()
        if tabel_card_swap == 'all':
            self.card_switch_all()
            swap_work = self.tabel_id.tabel_cards
            self.tabel_id.tabel_cards = self.cardes
            self.cardes = swap_work
        else:
            tabel_card_swap = int(tabel_card_swap)    
            print('Hand Card(1-3):')
            hand_card_swap= int(input())
            
            swap_work=self.cardes[hand_card_swap-1]
            self.cardes[hand_card_swap-1] = self.tabel_id.tabel_cards[tabel_card_swap-1]
            self.tabel_id.tabel_cards[tabel_card_swap-1] = swap_work
            
            return 'switch'
            
    def win_ceck(self):
        to_val = self.cardes[0][2] + self.cardes[1][2] + self.cardes[2][2]
        self.total_val = to_val
        last_card_type = -1
        if to_val == 31:
            for card in self.cardes:
                if last_card_type != card[0] and last_card_type != -1:
                    return False
                last_card_type = card[0]
            return True

class game:
    def __init__(self,  player_num=int()):
        self.player_num = player_num
        self.tabel_cards = list()
        self.player_ref = list()
        self.dev_mode = False

        self.game_setup()

    def game_setup(self):
        for x in range(self.player_num):
            self.player_ref.append(player_ob(id=x, game_ref = self))
        
        for player_s in self.player_ref:
            if player_s.player_name == 'DEV':
                self.dev_mode = True
        self.give_cards()
        self.tabel_cards_give()
        
        last_player_act = str()
        win = False
        closed = False
        player_on_turn = 0
        pass_cout = 0
        close_count = 0
        
        while not win:
            player_act = self.player_ref[player_on_turn].player_turn()
            if player_act == 'close':
                closed = True
            if closed:
                close_count += 1
                if close_count == self.player_num:
                    win = True
                    break
                    
            elif player_act == 'switch':
                pass
            
            if player_act == 'pass':
                if pass_cout > 0 and last_player_act != 'pass':
                    pass_cout = 0
                pass_cout += 1
                if pass_cout == self.player_num:
                    self.tabel_cards_give()
                    pass_cout = 0
                    
            player_on_turn+=1
            if player_on_turn >= self.player_num:
                player_on_turn = 0
            for player in self.player_ref:
                if player.win_ceck():
                    win = True
            last_player_act = player_act
        
        winner = object()
        win_val = 0
        for player in self.player_ref:
            if player.total_val > win_val:
                winner = player
                win_val = player.total_val
        print('Winner is:', winner.player_name)
        exit() 

    def give_cards(self):
        for player in self.player_ref:
            player.card_give()

    def tabel_cards_give(self):
        self.tabel_cards = [(random_card()),
                            (random_card()),
                            (random_card())]
        self.show_tabel_cards()
        
    def show_tabel_cards(self):
        print('Tabel Cards:')
        for x in range(len(self.tabel_cards)):
            print(self.tabel_cards[x][0], self.tabel_cards[x][1])
            

def random_card():
    while True:
        rand_num = rand.randint(0, len(game_cards)-1)
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
    if player_num > 1:
        spiel = game(player_num)
    else:
        exit()
        
