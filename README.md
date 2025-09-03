
🃏 Video Poker Game
A desktop-based Video Poker experience built with Python and PyQt5 – featuring hand evaluation, payouts, and a clean GUI.

🎮 Built by an upcoming developer & content creator – follow my journey as I build real-world projects, share tutorials, and grow in public!

🧩 Features
🃏 Deal a randomized 5-card hand from a standard 52-card deck
✅ Select cards to hold using checkboxes
🔄 Draw new cards to complete your final hand
🧠 Evaluate hand types (Flush, Straight, Full House, etc.)
💰 Calculate payouts based on hand strength and bet amount
🎉 Jackpot logic for Royal Flush with max bet
🖥️ GUI built with PyQt5 for a clean, responsive desktop experience

📦 Project Structure
├── main.py           # GUI and game flow logic
├── Logic.py          # Poker deck handling and hand evaluation
├── Payout.py         # Payout calculation based on hand strength and bet

🚀 Getting Started
✅ Requirements
Python 3.x
PyQt5
📦 Installation
pip install PyQt5
▶️ Run the Game
python main.py

🎥 Demo
Check out the full gameplay walkthrough on YouTube:
📺 [https://www.youtube.com/@CodeArcade-xq4]

🧠 How It Works
Poker Class (Logic.py)
Creates and shuffles a 52-card deck
Deals hands and replaces cards based on user holds
PokerHandEvaluator (Logic.py)
Detects hand types: Flush, Straight, Full House, etc.
Handles edge cases (Ace-low straights, Royal Flushes)
PokerPayoutCalculator (Payout.py)
Maps hand types to payout multipliers
Calculates winnings based on bet
Jackpot logic: Royal Flush + $5 bet = 💰 $4000
Example:
calculator = PokerPayoutCalculator("Full House", 3)
print(calculator.calculate_payout())  # Output: 27

🛠️ Customization Ideas
🎴 Add card images or animations
💹 Expand payout tiers or introduce progressive jackpots
📊 Track player stats or win history
🔊 Add sound effects or a leaderboard

📣 Let’s Connect
If you enjoyed this project, want to collaborate, or just say hi:
🐦 Twitter: [@yourhandle]
📺 YouTube: [Your Channel]
💬 GitHub Issues for feedback & feature ideas
✉️ Email: [codearcade.dev11@gmail.com]

⭐ Star this repo to support the project
🔔 Follow me for more Python, game dev, and GUI-based projects!