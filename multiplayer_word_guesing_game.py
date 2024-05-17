import random

def randomWord():
    wordList = ['trash', 'apple', 'soccer', 'time', 'creative', 'awesome', 'bottle',
                'successful', 'neat', 'interested', 'story', 'cup', 'attention', 'shift', 'delete', 'return', 'okay']
    return random.choice(wordList)

number_of_players = int(input("Enter the number of players: "))
players = {}
for i in range(number_of_players):
    players[f"Player {i+1}"] = ''

def show_word(w, g):
    result = ''
    for char in w:
        if char in g:
            result += char
        else:
            result += '_'
    return result

def game():
    w = randomWord()
    max_tries = 10
    t = 0
    print("Welcome to the Word Guessing Game!")
    print("Guess the word, you have 10 attempts.")
    print("Good Luck!!")

    while t < max_tries:
        for p, g in players.items():
            print(f"\n{p}'s turn. What you see: {show_word(w, g)}")
            guess = input("Enter a letter: ").strip().lower()

            if guess in g or not guess.isalpha() or len(guess) != 1:
                print("Invalid input, enter a single alphabetical letter.")
                continue

            players[p] += guess
            if guess in w:
                print("Good guess!")
                if all(l in players[p] for l in w):
                    print(f"{p} good work you got it! The word was: {w}")
                    return
            else:
                print(f"Nope! {p} has " + str(max_tries - t - 1) + " tries left.")
        
        t += 1

    print("Oh no! Game over! The word was: " + w)

if __name__ == '__main__':
    game()
