class Card:
    _suits = ["пика", "черва", "бубна", "треф"]
    _values = [None, None, "2", "3",
              "4", "5", "6", "7", "8", "9",
              "10", "валет", "дама", "король", "туз"]

    def __init__(self, s, v):
        self.suit = s
        self.value = v

    def __repr__(self):
        v = self._suits[self.suit] + " " + self._values[self.value]
        return v

    def __lt__(self, c2):
        if self.value < c2.value:
            return True

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
