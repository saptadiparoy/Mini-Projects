import random as rdm

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit
    

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        for card in self.deck:
            deck_comp += "\n" + card.__str__()

    def shuffle(self):
        rdm.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        
        while self.value > 21 and self.aces > 0:
            self.value -=10
            self.aces += 1

"""test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print(test_player.value)
"""

class Chips :
    def __init__(self, total = 100):
        self.total = total 
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.bet

def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet?:   "))

        except:
            print ("Please provide an integer!")

        else:
            if chips.bet > chips.total:
                print ("Sorry, you have have enough chips. You have:    {}".format(chips.total))

            else:
                break

        
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? (H/S):     ").upper()
        if x == "H":
            hit(deck, hand)

        elif x == "S":
            print("Player Stands. Dealer's Turn")
            playing = False

        else:
            print("Invalid, Please enter H or S.")
            continue

        break

def show_some(player , dealer):
    print ("\nDealer's Hand:    ")
    print ("First card Hidden!")
    print (dealer.cards[1])

    print("\nPlayer's Hand:     ")
    for card in player.cards:
        print (card)



def show_all(player, dealer):
    print ("\nDealer's Hand:    ")
    for card in dealer.cards:
        print (card)

    print(f"Value of Dealer's hand:  {dealer.value}")

    print("\nPlayer's Hand:     ")
    for card in player.cards:
        print (card)

    print(f"Value of Player's hand:  {player.value}")

def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("BUST DEALER!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player, dealer):
    print ("Dealer and player tie! PUSH!")


while True:

    print("Welcome to Balck Jack!")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #setting player chips
    player_chips = Chips()

    #promt player for bet
    take_bet(player_chips)

    #show cards (keeping dealer's hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        #promt for player to hit or stand
        hit_or_stand(deck, player_hand)

        #show cards but keep one dealer card hidden
        show_some(player_hand, dealer_hand)

        #if player exceeds 21, run player_busts() and break loop
        if player_hand.value >21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    #if player hasnt busted, play dealers hand until dealer reaches 17:
    if player_hand.value < 21:

        while dealer_hand.value <17:
            hit(deck, dealer_hand)

        #show all cards
        show_all(player_hand , dealer_hand)

        #run diff winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    #inform player of their chips:
    print(f"\nPlayer total chips are at:     {player_chips.total}")

    new_game = input("Would you like to play again?(y/n):   ").lower()

    if new_game == "y":
        playing = True
        continue

    else:
        print("Thanks for playing!")
        break
