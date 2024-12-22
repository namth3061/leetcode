'''
You are given an integer array ranks and a character array suits. 
You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].

The following are the types of poker hands you can make from best to worst:

"Flush": Five cards of the same suit.
"Three of a Kind": Three cards of the same rank.
"Pair": Two cards of the same rank.
"High Card": Any single card.
Return a string representing the best type of poker hand you can make with the
 given cards.

Note that the return values are case-sensitive.
Example 1:

Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
Output: "Flush"
Explanation: The hand with all the cards consists of 5 cards with the same suit, 
so we have a "Flush".
Example 2:

Input: ranks = [4,4,2,4,3], suits = ["d","a","a","b","c"]
Output: "Three of a Kind"
Explanation: The hand with the first, second, and fourth card consists of 3 cards 
with the same rank, so we have a "Three of a Kind".
Note that we could also make a "Pair" hand but "Three of a Kind" is a better hand.
Also note that other cards could be used to make the "Three of a Kind" hand.
Example 3:

Input: ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
Output: "Pair"
Explanation: The hand with the first and second card consists of 2 cards with
the same rank, so we have a "Pair".
Note that we cannot make a "Flush" or a "Three of a Kind".
 

Constraints:

ranks.length == suits.length == 5
1 <= ranks[i] <= 13
'a' <= suits[i] <= 'd'
No two cards have the same rank and suit.
'''

from collections import Counter
from typing import List
import random


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        len_unique = len(set(suits))
        len_ranks = len(set(ranks))

        if self.checkError(ranks, suits) or max(ranks) > 13 or min(ranks) < 0:
            return "Not Found"
        
        rank_special = [1, 10, 11, 12 , 13]
        ranks.sort()

        firstRank = ranks[0]
     
        if len_unique == 1 and len_ranks == 5:
            return self.highestRank(ranks, rank_special,firstRank )
        else:
            if len_unique != 1:
                if ranks == rank_special or self.checkStraight(ranks, firstRank):
                    return "Straght"
                elif len_ranks == 4:
                    return "Pair"
                counter = Counter(ranks)
                duplicate = {number: count for number, count in counter.items() if count > 1}
                duplicate = list(duplicate.values())
                if len(duplicate) > 0:
                    if duplicate == [2,2]:
                        return "Two Pairs"
                    elif duplicate[0] == 3:
                        return "Three of a Kind"
                    elif sorted(duplicate) == [2,3] :
                        return "Full House"
                    elif duplicate[0] == 4:
                        return "Quads"


        return "High Card"
    
    def highestRank(self, ranks, rank_special, firstRank):
        if ranks == rank_special:
            return "Royal Straght Flush"
        
        if self.checkStraight(ranks, firstRank):
            return "Straght Flush"
        else:
            return "Flush"
        
    def checkStraight(self, ranks, firstRank):
        isStraight = True
        for i in range(1, 5):
            total = firstRank + i
            if total == ranks[i]:
                continue
            else:
                isStraight = False
        return isStraight

    def checkError(self, ranks, suits):
        notFound = False
        for i in range(0, 5):
            for j in range(4, -1, -1):
                if i == j:
                    continue
                if ranks[i] == ranks[j] and suits[i] == suits[j]:
                    notFound = True
                    break
        return notFound

def generate_poker_hand():
    pocker_hand = []  # To store card values
    suits = []        # To store card suits

    while len(pocker_hand) < 5:
        value = random.randint(1, 5)  # Random value between 1 and 13
        suit = random.choice(['s', 'd', 'h', 'c'])  # Random suit

        if (value, suit) not in zip(pocker_hand, suits):
            pocker_hand.append(value)
            suits.append(suit)

    return pocker_hand, suits


if __name__ == '__main__':
    s = Solution()

    ranks, suits = generate_poker_hand()
    print(ranks, suits)

    re = s.bestHand(ranks, suits)
    print(re)
