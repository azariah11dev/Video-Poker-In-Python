
# file 3: Payout.py
class PokerPayoutCalculator:
    # Each hand type maps to a payout multiplier (based on a $ bet)
    PAYOUT_TABLE = {
        "Royal Flush": 250,
        "Straight Flush": 50,
        "Four of a Kind": 25,
        "Full House": 9,
        "Flush": 6,
        "Straight": 4,
        "Three of a Kind": 3,
        "Two Pair": 2,
        "Pair": 1,        # Only counts if it's Jacks or Better
        "High Card": 0    # No payout for just a high card
    }

    def __init__(self, hand_type, bet_amount):
        """
        Initialize with:
        - hand_type: the name of the poker hand (e.g., "Flush", "Pair")
        - bet_amount: how much the player bet (usually $1–$5)
        """
        self.hand_type = hand_type
        self.bet_amount = bet_amount

    def calculate_payout(self):
        """
        Calculate the payout based on the hand type and bet amount.
        Uses the payout table to find the multiplier.
        """
        # Get the multiplier for the hand type (default to 0 if not found)
        multiplier = self.PAYOUT_TABLE.get(self.hand_type, 0)

        # Multiply the bet amount by the payout multiplier
        payout = multiplier * self.bet_amount

        # 🎉 Special case: Royal Flush with max bet ($5) triggers jackpot
        if self.hand_type == "Royal Flush" and self.bet_amount == 5:
            payout = 4000  # Flat jackpot payout

        return payout