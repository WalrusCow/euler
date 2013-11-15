FILE = 'problem54.txt'

class Card():
    RANK_STR = '23456789TJQKA'
    def __init__(self, cardStr):
        self.rank = Card.RANK_STR.find(cardStr[0])
        self.suit = cardStr[1]

class Hand():
    def __init__(self, cardList):
        self.cards = [Card(c) for c in cardList]
        self.getHandRank()

    def _getHandRank(self):
        '''
        All ranks are represented as lists,
        the first item of which is a tuple, followed by
        the cards, sorted in order.

        High card = (0, )
        Pair = (1, PV)
        2Pair = (2, PV1, PV2)
        3Kind = (3, card)
        Straight = (4,)
        Flush = (5,)
        3Kind + Pair = (6, 3KV, PV)
        4Kind = (7, KV)
        Straight Flush = (8,)
        Royal Flush = (9,)
        '''

        pass

def findHandRank(hand):
    # If Four of a kind:
    # If 3 of a Kind + one Pair
    # If All Same Suit
        # If Consecutive
            # If royal
    # If consecutive
    # If 3 of a kind
    # if 2 pairs
    # if one pair
    # High card

    pass

def winner(p1, p2):
    pass


def solve():
    p1Wins = 0
    with open(FILE) as f:
        for line in f:
            cards = line.split()
            p1 = Hand(cards[:5])
            p2 = Hand(cards[5:])

            if winner(p1, p2) == 1:
                p1Wins += 1
    return p1Wins
