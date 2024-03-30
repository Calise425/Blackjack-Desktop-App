# Blackjack Game

This is a simple implementation of the classic card game Blackjack using Python's Tkinter library for the GUI.
Assets are all hand-drawn by me! 

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/blackjack-game.git
    ```

2. Navigate to the project directory:

    ```bash
    cd blackjack-game
    ```

3. Install the required dependencies. Ensure you have Python installed on your system.

4. Run the game:

    ```bash
    python blackjack.py
    ```

## How to Play

1. When you run the game, you'll see a window pop up with the Blackjack table displayed.
2. Click the "Hit Me" button to draw a card.
3. Click the "Hold" button to end your turn and let the dealer play.
4. Try to get as close to 21 as possible without going over.
5. If you go over 21, you bust and lose the game.
6. The dealer will then reveal their cards and play their turn.
7. The game will automatically determine the winner and display the result.

## Features

- Simple and intuitive GUI interface using Tkinter.
- Player-friendly controls with "Hit Me" and "Hold" buttons.
- Automatic determination of the winner based on Blackjack rules.

## Dependencies

- Python 3.x
- Tkinter

## Contributing

Contributions are welcome! Feel free to open a pull request or submit an issue if you encounter any bugs or have suggestions for improvements.

## Wishlist/ TODO

- I love the idea of making betting possible in some way, and tracking current chips
- I want to include the ability to double down or split your hand (but both probably don't make sense until you can bet)
- Make the play again button function better (currently when a new game starts I just send it way off-screen T-T)