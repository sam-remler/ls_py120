import urllib3
import re
import random

class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.color = 'N'  # N = None, G = Green, Y = Yellow

    def __str__(self):
        return f"{self.letter} ({self.color})"

class Guess:
    def __init__(self, word):
        self.word = word
        self.letters = [Letter(letter) for letter in word]

    def __str__(self):
        return " ".join([str(letter) for letter in self.letters])

    def check_guess(self, hidden_word):
        hidden_word_list = list(hidden_word)  
        guess_letters = [letter.letter for letter in self.letters]
        
        # First pass: Check for correct letters in correct positions (Green)
        for index, letter in enumerate(self.letters):
            if hidden_word[index] == letter.letter:
                letter.color = 'G'
                hidden_word_list[index] = None  # Mark used letters
        
        # Second pass: Check for correct letters in wrong positions (Yellow)
        for index, letter in enumerate(self.letters):
            if letter.color != 'G' and letter.letter in hidden_word_list:
                letter.color = 'Y'
                hidden_word_list[hidden_word_list.index(letter.letter)] = None  # Mark as used


class Board:
    def __init__(self, word_list):
        self.hidden_word = random.choice(word_list)
        self.guesses = []
        self.max_attempts = 6

    def is_won(self):
        return self.guesses and self.guesses[-1].word == self.hidden_word

    def is_lost(self):
        return len(self.guesses) >= self.max_attempts

    def display(self):
        for guess in self.guesses:
            print(guess)

    def remaining_attempts(self):
        return self.max_attempts - len(self.guesses)


class Wordle:
    def __init__(self):
        self.words = self.create_word_list()
        self.board = Board(self.words)

    def create_word_list(self):
        """Fetch a list of 5-letter words from an online source."""
        http = urllib3.PoolManager()
        url = "https://www.wordfrequency.info/samples/lemmas_60k.txt"
        response = http.request("GET", url)
        text = response.data.decode("utf-8")

        words = re.findall(r"\b[a-zA-Z']+\b", text)
        return [word.lower() for word in words if len(word) == 5 and word.isalpha()]

    def welcome_message(self):
        print("Welcome to Wordle! Guess the 5-letter word in 6 tries.")

    def make_guess(self):
        while True:
            guess = input(f"Enter your guess ({self.board.remaining_attempts()} attempts left): ").lower()
            if len(guess) != 5 or guess not in self.words:
                print("Invalid guess. Please enter a valid 5-letter word.")
            else:
                break

        guess_obj = Guess(guess)
        self.board.guesses.append(guess_obj)
        guess_obj.check_guess(self.board.hidden_word)

    def play(self):
        self.welcome_message()
        while not self.board.is_won() and not self.board.is_lost():
            self.make_guess()
            self.board.display()

        if self.board.is_won():
            print(f"Congratulations! You guessed the word '{self.board.hidden_word}'.")
        else:
            print(f"Game over. The word was '{self.board.hidden_word}'.")



game = Wordle()
game.play()

