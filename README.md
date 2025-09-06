# Python Snake Game 🐍

A classic Snake game implementation in Python using Pygame with smooth gameplay, score tracking, and restart functionality.

## Features

- **Smooth Gameplay**: 10 FPS for optimal game experience
- **Score Tracking**: Earn 10 points for each food item consumed
- **Visual Design**: 
  - Green snake with darker head
  - Red food items
  - Grid-based movement system
- **Game Controls**: Arrow keys for movement
- **Game Over Handling**: Restart with spacebar or quit with escape
- **Collision Detection**: Wall and self-collision detection

## Requirements

- Python 3.6+
- Pygame library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/charliebravo110/python-snake-game.git
cd python-snake-game
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

1. Run the game:
```bash
python snake_game.py
```

2. **Controls**:
   - **Arrow Keys**: Move the snake (Up, Down, Left, Right)
   - **Spacebar**: Restart game (when game over)
   - **Escape**: Quit game (when game over)

3. **Objective**: 
   - Guide the snake to eat the red food items
   - Each food item increases your score by 10 points
   - Avoid hitting the walls or the snake's own body
   - The snake grows longer with each food item consumed

## Game Mechanics

- **Grid System**: 800x600 pixel window with 20x20 pixel grid cells
- **Snake Movement**: Moves one grid cell per frame
- **Food Generation**: Random placement, avoiding snake body
- **Growth**: Snake grows by one segment per food item
- **Game Over Conditions**:
  - Hitting the window boundaries
  - Colliding with the snake's own body

## Code Structure

- `Snake` class: Handles snake movement, growth, and rendering
- `Food` class: Manages food placement and rendering
- `Game` class: Main game loop, event handling, and game state management

## Screenshots

The game features a clean, minimalist design with:
- Black background
- Green snake with darker green head
- Red food items
- White score display
- Game over screen with restart instructions

## Contributing

Feel free to fork this repository and submit pull requests for improvements such as:
- Additional game features (power-ups, obstacles)
- Enhanced graphics or animations
- Sound effects
- High score persistence
- Different difficulty levels

## License

This project is open source and available under the MIT License.

## Author

Created by charliebravo110

---

Enjoy playing the classic Snake game! 🎮
