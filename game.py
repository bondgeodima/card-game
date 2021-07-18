from deck import Deck
from player import Player


class Game:
    def __init__(self):
        _name1 = input("Введіть імя першого гравця: ")
        _name2 = input("Введіть імя другого гравця: ")
        self.deck = Deck()
        self.p1 = Player(_name1)
        self.p2 = Player(_name2)

    def _winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Нічья"

    def _wins(self, p1, p2, p1c, p2c):
        if p1c > p2c:
            print("{} забрав карти".format(self.p1.name) + "\n")
            self.p1.wins += 1
        else:
            print("{} забрав карти".format(self.p2.name) + "\n")
            self.p2.wins += 1

    def play_game(self):
        cards = self.deck.cards
        print (len(cards))
        print ("Починаємо")
        while len(cards) >= 2:
            m = "Введіть Х для виходу. Для продовження натисніть іншу клавішу: "
            response = input(m)
            if response == 'x':
                break
            p1c = cards.pop()
            p2c = cards.pop()
            print ("Ігрок {} достав карту {}. Ігрок {} достав карту {}".format(self.p1.name, p1c, self.p2.name, p2c))

            self._wins(self.p1, self.p2, p1c, p2c)

        win = self._winner(self.p1, self.p2)
        print ("{} виграв".format(win))

