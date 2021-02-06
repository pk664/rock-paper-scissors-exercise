# rock-paper-scissors-exercise

A Python application that allows a human user to play a fun game of rock, paper, and scissors against a computer (NPC) opponent. 

# Prerequisites 

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](http://github.com/pk664/rock-paper-scissors-exercise) under your own control, then "clone" or download your remote copy onto your local computer.


After cloning the repo, navigate there from the command-line:

```sh
cd rock-paper-scissors-exercise
```

Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

```sh
conda create -n my-game-env python=3.8
conda activate my-game-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## User Name Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username. For example: 

    USER_NAME="John Snow"

If no username is specified by the player, then the default name of the user in the game would be "Player One." 

## Usage

Run the game script by executing the following command: 

```py
python game.py

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", 
it's because the given package isn't installed, so run the `pip` command above to ensure that 
package has been installed into the virtual environment. 

The following rules apply to the game: 

1. Rock beats Scissors
2. Paper beats Rock
3. Scissors beats Paper
4. Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

Good luck and have fun playing the game! 