import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                pass
    
    
    def __str__(self):
        return '\n'.join(str(card) for card in self.deck)
        pass

    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
    pass

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0  
        self.aces = 0   
         
    def add_card(self,card):
        self.card = card
        self.cards.append(card)
        self.value += card.value
        
        if card.rank == 'Ace':
            self.aces += 1
        pass
    
    def adjust_for_ace(self):
         while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            pass
        
class Chips:
    
    def __init__(self):
        self.total = 100 
        self.bet = 0
        
    def win_bet(self):
        self.total = self.total + self.bet
        pass
    
    def lose_bet(self):
        self.total = self.total - self.bet
        pass
    
    def __str__(self):
        return f"Current balance: {self.total} chips"
    
    
def take_bet(player_chips):
    while True:
        try:
            btamount = int(input("Enter the amout you would like to bet on here: "))
            if btamount > player_chips.total:
                print(f"Insufficient chips! You have {player_chips.total} chips.")
            elif btamount <= 0:
                print("Bet must be greater than zero.")
            else:
                player_chips.bet = btamount
                break
        except ValueError:
            print("You didn't enter a number, try again")

def hit(deck,hand):
    card = deck.deal()
    hand.add_card(card)

    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing 
    
    decision = input("Would you like to hit or stand (h or s): ")
    if decision == 'h':
        hit(deck,hand)
    elif decision == 's':
        print("Player stands. Dealer's turn.")
        playing = False
    else:
        print("Invalid input. Please enter h or s.")
        
    pass


def show_some(player_hand,dealer_hand):
    print("Player's hand: ")
    for card in player_hand.cards:
        print(card)
    

    print("\nDealer's up card: ")
    print(dealer_hand.cards[0])

    
def show_all(player_hand,dealer_hand):
    print("Player's hand: ")
    for card in player_hand.cards:
        print(card)
    print("Total Value: ", player_hand.value)
        
    print("Dealer's hand: ")
    for card in dealer_hand.cards:
        print(card)
    print("Total Value: ", dealer_hand.value)
    pass


def player_busts(player_chips):
    print("Player busts!")
    player_chips.lose_bet()
    
def player_wins(player_chips):
    print("Player wins!")
    player_chips.win_bet()


def dealer_busts(player_chips):
    print("Dealer busts!")
    player_chips.win_bet()


def dealer_wins(player_chips):
    print("Dealer wins!")
    player_chips.lose_bet()


def push():
    print("It's a tie! Push.")

while True:

    print("Hey, welcome to BlackJack")

    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    dealer_hand = Hand()
    
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_chips = Chips()
    print(player_chips.total)
    
    take_bet(player_chips)
    
    
    show_some(player_hand,dealer_hand)
    
    while playing:          
        
        hit_or_stand(deck,player_hand)
        
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_chips)
        else:
            push()
            
    print("\nPlayer's total is", player_chips.total)
    new = input("Would you like to play again: (y or n)").lower()
    if new == "y":
        playing = True
    else:
        print("Thanks for playing!")
        break