import sys
from collections import Counter

# Ranks for hands (index lookup)
HAND_RANKS = ['HIGH_CARD', 'PAIR', 'TWO_PAIR', 'THREE_KIND', 'STRAIGHT',
              'FLUSH', 'FULL_HOUSE', 'FOUR_KIND', 'STRAIGHT_FLUSH',
              'ROYAL_FLUSH']

class Card():
    # Blank at start to make sure that all ranks are positive
    RANK_STR = ' 23456789TJQKA'
    def __init__(self, cardStr):
        self.rank = Card.RANK_STR.find(cardStr[0])
        self.suit = cardStr[1]


class Hand():
    def __init__(self, cardList):
        self.cards = [Card(c) for c in cardList]
        #self.cards.sort(key=lambda c: c.rank, reverse=True)
        self.rank = self._getHandRank()

    @staticmethod
    def _nKind(cards, n):
        ''' Check if cards has n of a kind. '''
        c = Counter(card.rank for card in cards)
        for rank, count in c.items():
            if count == n:
                return rank
        return None

    @staticmethod
    def fourKind(cards):
        return Hand._nKind(cards, 4)

    @staticmethod
    def threeKind(cards):
        return Hand._nKind(cards, 3)

    @staticmethod
    def pair(cards):
        return Hand._nKind(cards, 2)

    @staticmethod
    def fullHouse(cards):
        three = Hand.threeKind(cards)
        if three:
            # Look for two that aren't in the three
            two = Hand.pair(c for c in cards if c.rank != three)
            if two:
                return three, two
        return None

    @staticmethod
    def straight(cards):
        ''' Are all cards consecutive? '''
        ranks = sorted(c.rank for c in cards)
        last = ranks[0]
        for r in ranks[1:]:
            if r != last + 1:
                return None
            last = r
        return True

    @staticmethod
    def flush(cards):
        ''' Are all cards same suit? '''
        s = set(c.suit for c in cards)
        return True if len(s) == 1 else None

    @staticmethod
    def royal(cards):
        ''' Is it royal? (T, J, Q, K, A) '''
        minRank = Card.RANK_STR.index('T')
        return all(c.rank >= minRank for c in cards)

    @staticmethod
    def twoPair(cards):
        p1 = Hand.pair(cards)
        if p1:
            p2 = Hand.pair(c for c in cards if c.rank != p1)
            if p2:
                return (max(p1, p2), min(p1, p2))
        return None

    def _getHandRank(self):
        ''' Return a tuple.  '''

        rank = Hand.fourKind(self.cards)
        if rank:
            return HAND_RANKS.index('FOUR_KIND'), rank

        rank = Hand.fullHouse(self.cards)
        if rank:
            return (HAND_RANKS.index('FULL_HOUSE'), ) + rank

        rank = Hand.flush(self.cards)
        if rank:
            if Hand.royal(self.cards):
                # Flush + royal
                return (HAND_RANKS.index('ROYAL_FLUSH'), )
            if Hand.straight(self.cards):
                # Flush + straight
                return (HAND_RANKS.index('STRAIGHT_FLUSH'), )
            return (HAND_RANKS.index('FLUSH'), )

        rank = Hand.straight(self.cards)
        if rank:
            return (HAND_RANKS.index('STRAIGHT'), )

        rank = Hand.threeKind(self.cards)
        if rank:
            return HAND_RANKS.index('THREE_KIND'), rank

        rank = Hand.twoPair(self.cards)
        if rank:
            return (HAND_RANKS.index('TWO_PAIR'), ) + rank

        rank = Hand.pair(self.cards)
        if rank:
            return HAND_RANKS.index('PAIR'), rank

        return (HAND_RANKS.index('HIGH_CARD'), )


def winner(hand1, hand2):
    '''
    Determine the winner of two hands.
    Ties not accounted for properly.
    '''
    if hand1.rank > hand2.rank:
        return 1
    elif hand1.rank < hand2.rank:
        return 2
    # Hand ranks are the same - we go by highest card rank
    ranks1 = sorted((c.rank for c in hand1.cards), reverse=True)
    ranks2 = sorted((c.rank for c in hand2.cards), reverse=True)
    if ranks1 > ranks2:
        return 1
    return 2

def solve():
    p1Wins = 0
    for line in sys.stdin:
        cards = line.split()
        p1 = Hand(cards[:5])
        p2 = Hand(cards[5:])

        if winner(p1, p2) == 1:
            p1Wins += 1
    return p1Wins

if __name__ == '__main__':
    print(solve())
