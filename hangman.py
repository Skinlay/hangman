import getpass
import sys


class Hangman:

    def __init__(self):
        self.lives = 12

    def play(self):
        self.input_word()
        self.under_score()
        self.compare_input()
        self.amount_of_lives()

    def input_word(self):
        print("Hallo welcome to the hangman game.")
        # User inputs a word
        # getpass will make sure the input wont be visible
        answer = getpass.getpass("why don't you give me a word?:")
        # Makes a list of the word the user inputted
        self.list_of_letters = list(answer)
        # Counts the objects in the list
        self.number_of_letters = len(self.list_of_letters)
        print("The other player will have", self.lives, "attempts to guess this", self.number_of_letters, "-letter word")

    def under_score(self):
        print("_ " * self.number_of_letters)

    def compare_input(self):
        letter = input()
        list_letter = list(letter)
        # If it is a letter
        if list_letter < self.list_of_letters:
            # check if its in the word
            if letter in self.list_of_letters:
                print("true")
            else:
                self.lives = self.lives - 1
                print("fals")
        # Checks if the given words are the same
        elif list_letter == self.list_of_letters:
            print("correct you win")
            sys.exit(0)
        else:
            self.lives = self.lives - 1
            print("nee")

    def amount_of_lives(self):
        while self.lives > 0:
            print(self.lives)
            self.compare_input()
        else:
            print("you failed")
            sys.exit(0)

# TODO  show letters you guest correct
# TODO  place letter on correct position
# TODO  exit when all letter are guessed correct OR you will just need to enter the whole word
# TODO  make drawings of the hanging man
# TODO  show correct drawings of the hangman with the amount of lives left


if __name__ == '__main__':
    a = Hangman()
    a.play()



