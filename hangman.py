import getpass
import sys


class Hangman:

    def __init__(self):
        self.lives = 10
        self.correctly_guessed = []
        self.wrong_guessed = []
        self.wrong_letter = ""
        self.correct_letter = ""

    def play(self):
        self.input_word()
        while self.lives > 0:
            self.under_score()
            self.compare_input()
            self.amount_of_lives()
        else:
            self.failed()

    def input_word(self):
        print("Hallo welcome to the hangman game.")
        # User inputs a word
        # getpass will make sure the input wont be visible
        self.answer = getpass.getpass("why don't you give me a word?:")
        # Makes a list of the word the user inputted
        self.list_of_letters = list(self.answer)
        # Counts the objects in the list
        self.number_of_letters = len(self.list_of_letters)
        print("The other player will have", self.lives, "attempts to guess this", self.number_of_letters, "-letter word")

    def under_score(self):
        for letter in self.list_of_letters:
            if letter in self.correctly_guessed:
                print(letter+" ", end="")
            else:
                print("_ ", end="")
        print()

    def compare_input(self):
        letter = input()
        list_letter = list(letter)
        print(letter)
        print(list_letter)
        # If it is a letter
        if len(list_letter) == 1:
            # check if its in the word
            if letter in self.list_of_letters:
                print("true")
                self.saved_letters(letter, True)
            else:
                print("false")
                self.lives = self.lives - 1
                self.saved_letters(letter, False)
        # Checks if the given words are the same
        elif list_letter == self.list_of_letters:
            print("correct you win")
            sys.exit(0)
        else:
            print("nope")
            self.lives = self.lives - 1

    def saved_letters(self, letter, correct):
        if correct:
            self.correctly_guessed.append(letter)
        else:
            self.wrong_guessed.append(letter)
        print(self.correctly_guessed)
        print(self.wrong_guessed)

    def amount_of_lives(self):
        if self.lives == 10:
            print("--------------------------")
            print("|                        |")
            print("|                        |")
            print("|                        |")
            print("|                        |")
            print("|                        |")
            print("|                        |")
            print("|                        |")
            print("|                        |")
            print("|                        |")
            print("|                        |")
            print("--------------------------")

        elif self.lives == 9:
            print("--------------------------")
            print("|                        |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |___________________  |")
            print("|                        |")
            print("--------------------------")
        elif self.lives == 8:
            print("--------------------------")
            print("|  ____________________  |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |___________________  |")
            print("|                        |")
            print("--------------------------")
        elif self.lives == 7:
            print("--------------------------")
            print("|  ____________________  |")
            print("|  |/                    |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |___________________  |")
            print("|                        |")
            print("--------------------------")
        elif self.lives == 6:
            print("--------------------------")
            print("|  ____________________  |")
            print("|  |/          |         |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |___________________  |")
            print("|                        |")
            print("--------------------------")
        elif self.lives == 5:
            print("--------------------------")
            print("|  ____________________  |")
            print("|  |/          |         |")
            print("|  |           O         |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |___________________  |")
            print("|                        |")
            print("--------------------------")
        elif self.lives == 4:
            print("--------------------------")
            print("|  ____________________  |")
            print("|  |/          |         |")
            print("|  |           O         |")
            print("|  |           |         |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |___________________  |")
            print("|                        |")
            print("--------------------------")
        elif self.lives == 3:
            print("--------------------------")
            print("|  ____________________  |")
            print("|  |/          |         |")
            print("|  |           O         |")
            print("|  |          /|         |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |___________________  |")
            print("|                        |")
            print("--------------------------")
        elif self.lives == 2:
            print("--------------------------")
            print("|  ____________________  |")
            print("|  |/          |         |")
            print("|  |           O         |")
            print("|  |          /|\        |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |___________________  |")
            print("|                        |")
            print("--------------------------")
        elif self.lives == 1:
            print("--------------------------")
            print("|  ____________________  |")
            print("|  |/          |         |")
            print("|  |           O         |")
            print("|  |          /|\        |")
            print("|  |          /          |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |___________________  |")
            print("|                        |")
            print("--------------------------")

    def failed(self):
        print("--------------------------")
        print("|  ____________________  |")
        print("|  |/          |         |")
        print("|  |           O         |")
        print("|  |          /|\        |")
        print("|  |          / \        |")
        print("|  |                     |")
        print("|  |                     |")
        print("|  |___________________  |")
        print("|                        |")
        print("--------------------------")
        print("you failed, the word was", self.answer)


# TODO  exit when all letter are guessed correct OR you will just need to enter the whole word
# TODO change dwawing upper line to lower case one line higher
# TODO  do not show guessed letters multipul times


if __name__ == '__main__':
    a = Hangman()
    a.play()



