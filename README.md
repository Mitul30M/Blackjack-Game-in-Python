# Blackjack Game in Python

This project is a console-based implementation of the classic Blackjack card game, enhanced with a chip betting system. Developed in Python, it offers a simple yet engaging experience for users who enjoy traditional card games. The objective is to beat the dealer by achieving a hand total closest to 21 without going over.

## Features

- **Chip Betting System**: Players start with a balance of 1500 chips and can bet at the beginning of each round. Wins and losses adjust the chip balance accordingly.
  
- **Card Dealing and Shuffling**: Cards are drawn randomly from a standard deck, with shuffling at the start of each round to ensure fairness.

- **Game Mechanics**:
  - Option to "Hit" (take a new card) or "Stand" (keep current hand).
  - Dealer draws until reaching at least 17.
  - Aces can be 1 or 11, helping to optimize the hand total.

- **Round Outcomes**:
  - Win by having a hand total closer to 21 than the dealer's without busting.
  - Lose by busting (exceeding 21) or if the dealer's hand is closer to 21.
  - Draws return the bet to the player.

- **Automatic Game End**: The game automatically ends if either player or dealer runs out of chips, with a message indicating the winner.

- **Console Management**: Clears the console at the start of each new round for clarity.

## How to Play

1. **Starting the Game**:
   - Run the script to initiate, with both player and dealer starting at 1500 chips.

2. **Betting**:
   - Enter your bet at the start of each round. Your balance updates based on the round's result.

3. **Gameplay**:
   - You and the dealer each receive two cards, with one dealer card visible.
   - Choose to "Hit" or "Stand" based on your hand's total.
   - The dealer plays according to fixed rules, drawing cards until reaching at least 17.

4. **Round Outcome**:
   - After the round, your chips are updated based on whether you win, lose, or draw.
   - You are prompted to continue or end the game based on your chip balance.

5. **End of the Game**:
   - The game concludes if you or the dealer's chips are depleted, with a final winner announced.

## Prerequisites

Before running the Blackjack game, ensure that your system meets the following requirements:

- **Python Installation**: Python 3.x installed. You can download it from [Python.org](https://www.python.org/downloads/).
- **Command Line Tool**: Access to a command line tool (e.g., Terminal on macOS and Linux, Command Prompt or PowerShell on Windows).

## Setup

To get started with this Blackjack game:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blackjack-game.git
  
2. Navigate to the project directory:
   ```bash
   cd blackjack-game
   ```
   
3. Run the game:
  ```bash
  python blackjack.py
  ```

<b>Enjoy the game, and feel free to contribute to its development!</b>




