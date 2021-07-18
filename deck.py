from card import Card
from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(2, 15):
                self.cards.append(Card(i, j))
        shuffle(self.cards)


# deck = Deck()
# for card in deck.cards:
#     print(card)
