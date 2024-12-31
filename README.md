# Space Shooter Game

This is a simple space shooter game built using Pygame.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/space_shooter.git
    cd space_shooter
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Game

To run the game, execute the following command:
```sh
python3 code/main.py
```

### Controls

- **Arrow Keys**: Move the player
- **Escape**: Quit the game

### Code Overview

The main game logic is contained in [main.py](code/main.py). Below is an explanation of the code:

### Explanation

- **Initialization**: The game initializes Pygame and sets up the display surface with a specified width and height.
- **Loading Assets**: Images for the player, stars, meteors, and lasers are loaded and converted to a format suitable for Pygame.
- **Event Loop**: The main game loop runs while the `running` variable is `True`. It handles events such as quitting the game or pressing the escape key.
- **Player Movement**: The player's direction is determined by the arrow keys, and the player's position is updated accordingly.
- **Drawing Sprites**: The display surface is filled with a background color, and all game sprites (stars, meteors, lasers, player) are drawn on the screen.
- **Updating the Display**: The display is updated to reflect the changes made during each iteration of the game loop.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.