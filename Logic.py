
#file 2
import random  # Used to shuffle the deck and randomize hands

class Poker:
    def __init__(self):
        # Define the four suits and thirteen ranks in a standard deck
        self.suits = ['♠', '♥', '♦', '♣']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # Create the full deck of 52 cards
        self.deck = self.create_deck()

    def create_deck(self):
        """Create a standard 52-card deck by combining each rank with each suit."""
        return [f"{rank}{suit}" for suit in self.suits for rank in self.ranks]

    def deal_hand(self):
        """Shuffle the deck and deal the first 5 cards as a hand."""
        random.shuffle(self.deck)  # Randomize the order of cards
        hand = self.deck[:5]       # Take the first 5 cards
        self.deck = self.deck[5:]  # Remove those cards from the deck
        return hand

    def draw_new_cards(self, hand, hold_indices):
        """
        Replace cards that are not held.
        hold_indices: list of positions (0–4) that the player wants to keep.
        """
        new_hand = []
        for i in range(5):
            if i in hold_indices:
                # Keep the original card at this position
                new_hand.append(hand[i])
            else:
                # Replace with the next card from the deck
                new_hand.append(self.deck.pop(0))
        return new_hand

from collections import Counter  # Helps count how many times each rank appears

class PokerHandEvaluator:
    # Map each rank to a numerical value for comparison
    RANK_VALUES = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    def __init__(self, hand):
        self.hand = hand
        # Extract ranks and suits from the hand
        self.ranks, self.suits = self.parse_hand()
        # Count how many times each rank appears
        self.rank_counts = Counter(self.ranks)

    def parse_hand(self):
        """Split each card into its rank and suit."""
        ranks = []
        suits = []
        for card in self.hand:
            rank = card[:-1]  # All characters except the last one (e.g., '10' from '10♠')
            suit = card[-1]   # Last character is the suit (e.g., '♠')
            ranks.append(rank)
            suits.append(suit)
        return ranks, suits

    def is_flush(self):
        """Check if all cards have the same suit."""
        return len(set(self.suits)) == 1

    def is_straight(self):
        """Check if the ranks form a consecutive sequence."""
        values = sorted([self.RANK_VALUES[r] for r in self.ranks])
        # Special case: Ace can be low in a straight (A-2-3-4-5)
        if values == [2, 3, 4, 5, 14]:
            return True
        # Check if each card is one higher than the previous
        return all(values[i] - values[i-1] == 1 for i in range(1, 5))

    def detect_multiples(self):
        """Identify pairs, three-of-a-kind, four-of-a-kind, and full house."""
        counts = list(self.rank_counts.values())
        if 4 in counts:
            return "Four of a Kind"
        elif 3 in counts and 2 in counts:
            return "Full House"
        elif 3 in counts:
            return "Three of a Kind"
        elif counts.count(2) == 2:
            return "Two Pair"
        elif 2 in counts:
            return "Pair"
        return None  # No matching ranks

    def detect_straight_flush(self):
        """Check for Straight Flush or Royal Flush."""
        if self.is_flush() and self.is_straight():
            # Royal Flush is a special case of Straight Flush with highest cards
            if set(self.ranks) == {'10', 'J', 'Q', 'K', 'A'}:
                return "Royal Flush"
            return "Straight Flush"
        return None

    def evaluate(self):
        """Determine the best possible hand ranking."""
        # First, check for the strongest hands
        sf_result = self.detect_straight_flush()
        if sf_result:
            return sf_result

        # Then check for flush or straight
        if self.is_flush():
            return "Flush"
        if self.is_straight():
            return "Straight"

        # Then check for pairs, three-of-a-kind, etc.
        multiples_result = self.detect_multiples()
        if multiples_result:
            return multiples_result

        # If nothing matches, return the highest card
        return "High Card"