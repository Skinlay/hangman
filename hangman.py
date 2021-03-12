import getpass


class Hangman:

    def play(self):
        self.input_word()
        self.under_score()

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

if __name__ == '__main__':
    a = Hangman()
    a.play()



