README: Multiplayer Word Guessing Game
Description:

This program is a console-based multiplayer word guessing game. Each player tries to guess a randomly selected word by inputting letters. They have 10 attempts to guess the word correctly.

Features:

Imports
- `random`: This module is used to randomly select a word from a predefined list of words.

Function: `randomWord()`
- Randomly selects a word from a predefined list.
- Returns the selected word to be used in the game.

Function: `game()`
This is the main function where the gameplay logic is implemented.

1. Initialization:
   - `wordList`: A list of possible words from which the game will randomly select one for the players to guess.
   - `w`: A randomly chosen word from the `wordList` using `random.choice()`.
   - `players`: A dictionary where each key is a player name and the value is a string to keep track of the letters that have been guessed by that player.
   - `max_tries`: An integer set to 10, representing the number of guesses the players have before the game ends collectively.

2. Game Introduction:
   - The function starts by printing a welcome message and informing the players that they have 10 attempts to guess the word.

3. Gameplay Loop:
   - The game enters a `while` loop that continues as long as `max_tries` is greater than 0.
   - Each player takes turns within this loop:
   - The current state of the word is displayed, showing underscores (`_`) for unguessed letters and the actual letters for correctly guessed ones.
   - Each player is prompted to guess a letter.

4. Guess Input:
   - Players input their guesses. This input is checked for various conditions:
   - If the guess is already guessed, not a single alphabetical letter, or if multiple characters are entered, an error message is printed and the turn continues without decrementing `max_tries`.

5. Processing the Guess:
   - If the guessed letter is part of the word, the game prints "Good guess!" and checks if the word is fully guessed.
   - If all letters in the word have been guessed (checked using the `all()` function), a success message is displayed for the player who completed the word, and the game ends.
   - If the guessed letter is not part of the word, a message is printed showing the number of tries left.

6. Game Over:
   - If all players exhaust their tries (`max_tries == 0`), a game over message is displayed along with the correct word.

Main Block
- `if __name__ == '__main__':`
- This conditional ensures that the game starts only if the script is run as the main program, not when imported as a module in another script. It calls the `game()` function to start the game.

How to Run the Game:

The game will start with the on-screen instructions:
- The game will display a series of underscores representing the letters of the word to be guessed.
- Players take turns entering letters. Type a letter and press Enter.
- The game will update the display based on each player's input, showing any correctly guessed letters in their correct positions.
- If a guess is incorrect, the number of remaining tries will decrease.
- Continue guessing letters until:
- One player guesses the word correctly, or
- All players run out of tries.

When Game Ends:

The game concludes either when a player guesses the word correctly, or all players exhaust their 10 tries. Upon completion, the game will display the correct word if it wasn't guessed

  MIT License

Copyright (c) 2024 Hiyaw Birhanu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Archy and michael helped me by looking over and directing code.
Thank you Dr. Jackson for guiding me in writing my code.