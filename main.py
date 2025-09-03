
#file 1: main.py

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QLineEdit, QMessageBox, QCheckBox
)

# Import game logic and payout calculator from separate modules
from Logic import Poker, PokerHandEvaluator
from Payout import PokerPayoutCalculator

# Main game window class
class PokerGameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Poker")  # Set window title
        self.poker = Poker()                # Create a new Poker game instance
        self.hand = []                      # Store current hand of cards
        self.hold_checkboxes = []           # Checkboxes to hold cards
        self.card_labels = []               # Labels to display each card
        self.init_ui()                      # Build the user interface

    def init_ui(self):
        layout = QVBoxLayout()  # Main vertical layout for the window

        # Bet input section
        bet_layout = QHBoxLayout()
        self.bet_input = QLineEdit()
        self.bet_input.setPlaceholderText("Enter bet amount ($1 or higher)")
        bet_layout.addWidget(QLabel("Bet:"))
        bet_layout.addWidget(self.bet_input)
        layout.addLayout(bet_layout)

        # Deal button to get initial hand
        self.deal_button = QPushButton("Deal Hand")
        self.deal_button.clicked.connect(self.deal_hand)
        layout.addWidget(self.deal_button)

        # Card display area with "Hold" checkboxes
        self.card_area = QHBoxLayout()
        for _ in range(5):  # Create 5 card slots
            vbox = QVBoxLayout()
            label = QLabel("Card")          # Placeholder for card text
            checkbox = QCheckBox("Hold")    # Checkbox to hold card
            self.card_labels.append(label)
            self.hold_checkboxes.append(checkbox)
            vbox.addWidget(label)
            vbox.addWidget(checkbox)
            self.card_area.addLayout(vbox)
        layout.addLayout(self.card_area)

        # Draw button to replace unheld cards
        self.draw_button = QPushButton("Draw")
        self.draw_button.clicked.connect(self.draw_new_cards)
        layout.addWidget(self.draw_button)

        # Evaluate button to check hand type and payout
        self.eval_button = QPushButton("Evaluate Hand")
        self.eval_button.clicked.connect(self.evaluate_hand)
        layout.addWidget(self.eval_button)

        # Result label to show hand type and winnings
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)  # Apply the layout to the window

    def deal_hand(self):
        """Shuffle and deal a new hand of 5 cards."""
        self.poker = Poker()  # Reset the deck
        self.hand = self.poker.deal_hand()  # Get a new hand
        for i, card in enumerate(self.hand):
            self.card_labels[i].setText(card)         # Show card
            self.hold_checkboxes[i].setChecked(False) # Uncheck all holds
        self.result_label.setText("")  # Clear previous result

    def draw_new_cards(self):
        """Replace cards that are not held."""
        # Get indices of cards the player wants to keep
        hold_indices = [i for i, cb in enumerate(self.hold_checkboxes) if cb.isChecked()]
        # Replace unheld cards with new ones from the deck
        self.hand = self.poker.draw_new_cards(self.hand, hold_indices)
        for i, card in enumerate(self.hand):
            self.card_labels[i].setText(card)  # Update card display

    def evaluate_hand(self):
        """Evaluate the hand and calculate payout."""
        try:
            bet = int(self.bet_input.text())  # Convert bet input to integer
            if bet < 1:
                raise ValueError  # Reject bets less than $1
        except ValueError:
            # Show warning if bet is invalid
            QMessageBox.warning(self, "Invalid Bet", "Please enter a valid bet between $1 or higher.")
            return

        # Evaluate the hand type (e.g., Flush, Pair)
        evaluator = PokerHandEvaluator(self.hand)
        hand_type = evaluator.evaluate()

        # Calculate payout based on hand type and bet
        payout_calc = PokerPayoutCalculator(hand_type, bet)
        payout = payout_calc.calculate_payout()

        # Show result to the player
        self.result_label.setText(f"{hand_type} — You win ${payout}!")

# Entry point to launch the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PokerGameWindow()
    window.show()
    sys.exit(app.exec_())
