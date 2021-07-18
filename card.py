class Card:
    suits = ["пика", "черва", "бубна", "треф"]
    values = [None, None, "2", "3",
              "4", "5", "6", "7", "8", "9",
              "10", "валет", "дама", "король", "туз"]

    def __init__(self, s, v):
        self.suit = s
        self.value = v

    def __repr__(self):
        v = self.suits[self.suit] + " " + self.values[self.value]
        return v

    def __lt__(self, c2):
        if self.value < c2.value:
            return True

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
