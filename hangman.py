import getpass


class Hangman:

    def __init__(self):
        pass

    def play(self):
        self.input_word()
        self.under_score()
        self.compare_input()

    def input_word(self):
        print("Hallo welcome to the hangman game.")
        # User inputs a word
        # getpass will make sure the input wont be visible
        answer = getpass.getpass("why don't you give me a word?:")
        # Makes a list of the word the user inputted
        self.list_of_letters = list(answer)
        # Counts the objects in the list
        self.number_of_letters = len(self.list_of_letters)

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
        # Checks if the given words are the same
        elif list_letter == self.list_of_letters:
            print("correct you win")
        else:
            print("nee")


if __name__ == '__main__':
    a = Hangman()
    a.play()



