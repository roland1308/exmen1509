import random

hangman_parts = [
    "  ____\n |    |\n      |\n      |\n      |\n",
    "  ____\n |    |\n O    |\n      |\n      |\n",
    "  ____\n |    |\n O    |\n |    |\n      |\n",
    "  ____\n |    |\n O    |\n/|    |\n      |\n",
    "  ____\n |    |\n O    |\n/|\\   |\n      |\n",
    "  ____\n |    |\n O    |\n/|\\   |\n/     |\n",
    "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n"
]


class GetRandomWord:
    def __init__(self):
        self.words = ["pepe", "casa", "padre", "marido", "mujer", "hombre"]

    def get_word(self):
        # using ww variable just to show the word in debug
        ww = self.words[random.randint(0, len(self.words) - 1)]
        print(ww)
        return ww


class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed = []
        self.tries = 0
        self.count = 0

    def guess(self, letter):
        self.tries += 1
        if letter in self.guessed:
            print("You already guessed that letter")
        else:
            self.guessed.append(letter)
            if letter in self.word:
                print("You guessed the letter!")
                self.count += 1
            else:
                print("You guessed wrong!")

    def get_status(self):
        print("Guess the word:")
        for letter in self.word:
            if letter in self.guessed:
                print(letter, end="")
            else:
                print("_", end="")
        print('\n')

    def print_hangman(self):
        print(hangman_parts[self.tries+1])

    def check_if_player_won(self):
        if self.count == len(self.word):
            return True

    def check_if_player_lost(self):
        if self.tries == 6:
            return True


class PlayGame:
    def __init__(self):
        self.word = GetRandomWord().get_word()
        self.hanged = Hangman(self.word)

    def play(self):
        while True:
            self.hanged.get_status()
            letter = input("Guess a letter: ")
            self.hanged.print_hangman()
            self.hanged.guess(letter)
            if self.hanged.check_if_player_won():
                print("You won!")
                break
            if self.hanged.check_if_player_lost():
                print("You lost!")
                break
        print(self.word)


if __name__ == "__main__":
    PlayGame().play()
