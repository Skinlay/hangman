import getpass
import sys


class Hangman:

    def __init__(self):
        self.lives = 10

    def play(self):
        self.input_word()
        self.under_score()
        self.compare_input()
        self.amount_of_lives()

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
                print("fals")
                self.lives = self.lives - 1
        # Checks if the given words are the same
        elif list_letter == self.list_of_letters:
            print("correct you win")
            sys.exit(0)
        else:
            print("nee")
            self.lives = self.lives - 1

    def amount_of_lives(self):
        while self.lives > 0:
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
                print("|  |                     |")
                print("|  |                     |")
                print("|                        |")
                print("--------------------------")
            elif self.lives == 8:
                print("--------------------------")
                print("|                        |")
                print("|  |                     |")
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
                print("|                        |")
                print("|  |___________________  |")
                print("|  |                     |")
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
                print("|                        |")
                print("|  |___________________  |")
                print("|  |/                    |")
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
                print("|                        |")
                print("|  |___________________  |")
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
                print("|                        |")
                print("|  |___________________  |")
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
                print("|                        |")
                print("|  |___________________  |")
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
                print("|                        |")
                print("|  |___________________  |")
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
                print("|                        |")
                print("|  |___________________  |")
                print("|  |/          |         |")
                print("|  |           O         |")
                print("|  |          /|\        |")
                print("|  |          /          |")
                print("|  |                     |")
                print("|  |                     |")
                print("|  |___________________  |")
                print("|                        |")
                print("--------------------------")
            self.compare_input()
        else:
            print("--------------------------")
            print("|                        |")
            print("|  |___________________  |")
            print("|  |/          |         |")
            print("|  |           O         |")
            print("|  |          /|\        |")
            print("|  |          / \        |")
            print("|  |                     |")
            print("|  |                     |")
            print("|  |___________________  |")
            print("|                        |")
            print("--------------------------")
            print("you faled the word was", self.answer)


        # while self.lives > 0:
        #     print(self.lives)
        #     self.compare_input()
        # else:
        #     print("you failed")
        #     sys.exit(0)

# TODO  show letters you guest correct
# TODO  place letter on correct position
# TODO  exit when all letter are guessed correct OR you will just need to enter the whole word
# TODO  show the letters you guessed


if __name__ == '__main__':
    a = Hangman()
    a.play()



