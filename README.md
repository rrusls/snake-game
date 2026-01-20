# snake-game
A simple snake game created with Python and PySDL3 by rrusls (me). Made for enjoyment and to show my skills with PySDL3.

# Features
  - Interactive snake
  - Real-time vizualization using SDL3
  - Random apple occurences which can be eaten by snake
  - Console log whenever food is spawned, looks like "spawn food: (x, y)"

# Installation  
  1. Clone the repository:
     ```
     git clone https://github.com/rrusls/snake-game.git
     cd snake-game
     ```
  2. What you need to install:
     PySDL3
     ```
     pip install pysdl3
     pip install pysdl3-dll <- Windows
     ```
# Usage
  Run with:
  ```
  python snake-game.py
  ```
You can play with ticks, randoms and overall logic, etc. Just to make it more fun
## Optional conditions could include:
  - Custom non-black background
  - Ability to die because of borders / hitting itself
  - More accurate random (maybe???)
# Good to know
When running, there is a chance there would be some problems with the version of pySDL3. Make sure you install a PySDL3 version which is compatible. Mine is 0.9.8b1.

Also when running, interpretator can show messages like ```Warning: Version mismatch with binary: 'SDL3_net.dll' (expected: 3.0.0, got: none)```. It is safe to not care about this, program will start regardless.

The snake is pretty much immortal, since there is no logic of it's death, so you can make it endlessly. I thought it much more fun than dying.

Write, contribute, test. It's all will be appreciated anytime.

Thank you for reading.





