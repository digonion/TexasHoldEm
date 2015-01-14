"""
Will find results of hand

Pot odds:
    C = C / C + P
    C - Amount of money needed to call or raise
    P - Amount of money in the pot

Hand Strength:
    hand_strength^n
    n - Number of players

Call or Raise
    pot odds <= Hand strength

Probability triple:
    PT = f + c + r
    f - Fold
    c - Call
    r - Raise

Random strategy
    Choose fold, call, or raise by equal probability. If fold was selected and check is available then choose check

Simple strategy
    Always call if you can, never raise

Threshold strategy
    Raise if handstrength is greater than a given threshold, call if it is lower and still above another threshold

""" 


#!/usr/bin/env python3
import collections
import itertools
import random

SUIT_LIST = ("Hearts", "Spades", "Diamonds", "Clubs")
NUMERAL_LIST = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

######################### CLASSES #########################
class card:
    def __init__(self, numeral, suit):
        self.numeral = numeral
        self.suit = suit
        self.card = self.numeral, self.suit
    
    def __repr__(self):
        return self.numeral + "-" + self.suit

class Dealer(set):
    def __init__(self):
        for numeral, suit in itertools.product(NUMERAL_LIST, SUIT_LIST):
            self.add(card(numeral, suit))
    
    def get_card(self):
        """ Get single card """
        a_card = random.sample(self, 1)[0]
        self.remove(a_card)
        return a_card

def main():
    # Get my hand
    hand = {'card1': Dealer().get_card(), 'card2': Dealer().get_card()}
    
    
    
    return hand


if __name__ == '__main__':
    print main()
