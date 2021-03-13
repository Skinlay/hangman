import getpass


class Hangman:

    def __init__(self):
        pass

    def play(self):
        self.input_word()
        self.under_score()
        self.letter_in_list()

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

    def letter_in_list(self):
        letter = input()
        # Checks if the given letter is in the list of the word
        if letter in self.list_of_letters:
            print("true")
        else:
            print("fals")




if __name__ == '__main__':
    a = Hangman()
    a.play()



