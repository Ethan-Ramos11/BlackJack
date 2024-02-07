class Cards:
    suit = ""
    rank = 0

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        if self.suit == "♥" or self.suit == "♦":
            return colored(f"{self.rank} of {self.suit}", "red")
        else:
            return colored(f"{self.rank} of {self.suit}", "black")
