import cards
import random
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


class Deck:

    def __init__(self):
        self.resetDeck()

    def deck_str(self):
        str = ""
        for card in self.pile:
            str += f"{card}\n"
        return str

    def shuffle(self):
        return random.shuffle(self.pile)

    def drawCard(self):
        try:
            return self.pile.pop(0)
        except (IndexError):
            return None

    def drawHands(self, numPlayers):
        if numPlayers * 2 > len(self.pile):
            return "Not enough cards for number of players"
        hands = [[] for i in range(numPlayers)]
        for i in range(2):
            for j in range(numPlayers):
                hands[j].append(self.drawCard())
        return hands

    def getNumCardsLeft(self):
        return len(self.pile)

    def resetDeck(self):
        self.pile = []
        for suit in ["♠", "♣", "♥", "♦"]:
            for rank in ranks:
                self.pile.append(cards.Cards(suit, rank))
