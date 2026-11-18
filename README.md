Dice Game with Combination Rules and Chip Allocation

Overview

A Python-based two-player dice game featuring combination-based scoring and chip allocation. The project implements game logic, evaluates dice combinations, and simulates multiple rounds until the shared chip pool is empty.

Features

* Dice Combination Evaluation: Sorts dice rolls and identifies combinations such as three of a kind, straights, and the 4-2-1 combination.
* Scoring System: Converts dice combinations into chip values according to the game’s rules.
* Two-Player Gameplay: Runs a multi-round game between two players.
* Chip Allocation: Distributes chips from a shared pool according to the game outcomes.
* Terminal Interface: Uses Rich to improve the presentation of dice and game information in the console.

Technologies

* Python
* Rich

How to Run

1. Install the dependency

python -m pip install rich

2. Run the game

python dice_game.py

Replace dice_game.py with your actual Python filename if it is different.

Concepts Practiced

* Conditional logic and control flow
* Functions and modular program design
* Lists and sorting
* Random number generation
* Game-state management
* Rule-based scoring and simulation

Future Improvements

* Add automated tests for dice combinations and scoring rules.
* Separate the game logic from the terminal interface.
* Add configurable game rules and more detailed statistics.
