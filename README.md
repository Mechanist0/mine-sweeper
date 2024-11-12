# Minesweeper Game in Python

This project is a basic implementation of the classic Minesweeper game using Python and Pygame. It includes core game mechanics like mine placement, flagging, and win/loss conditions.
Features

    Randomized Mine Placement: Each game includes randomly placed mines across the grid.
    Flagging Mines: Right-click to flag a tile if you think it's a mine.
    Safe Zone Uncovering: Left-click on tiles to reveal them, with safe zones uncovering surrounding tiles.
    Win and Lose Conditions: Win by flagging all mines correctly; lose if you uncover a mine.

# Getting Started
## Prerequisites

    Python 3.x
    Pygame library (pip install pygame)

## Running the Game

    Clone this repository.
    Install dependencies using pip install -r requirements.txt.
    Run the game with:

    python main.py

## How to Play

    Left-Click: Reveal a tile. If it's a mine, you lose. If it has no nearby mines, surrounding tiles are also revealed.
    Right-Click: Flag a tile to mark it as a mine.