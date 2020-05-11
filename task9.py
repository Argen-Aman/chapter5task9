from random import shuffle, randint

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print(f'{self.value} {self.suit}')

class Deck(Card):
    def __init__(self):
        self.deck = []
        self.deal()

    def deal(self):
        for item in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            for i in ['червы', 'бубны', 'трефы', 'пики']:
                self.deck.append(Card(item, i))

    def mix(self):
        shuffle(self.deck)

    def r_card(self):
        indices = 51
        r = randint (0, indices)
        indices -= 1
        random_card = self.deck.pop(r)
        random_card.show()

deck = Deck()

deck.r_card()
