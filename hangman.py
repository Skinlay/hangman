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
        list_of_letters = list(answer)
        # Counts the objects in the list
        self.number_of_letters = len(list_of_letters)

    def under_score(self):
        underscore = "_"
        number_of_underscore = 0
        # prints underscores until thy are equal to the number of letters
        while self.number_of_letters != number_of_underscore:
            # Prints a underscore
            # "end" ensures the underscores are printed next to each other
            print(underscore, end=" ")
            # adds 1 to variable
            number_of_underscore += 1

if __name__ == '__main__':
    a = Hangman()
    a.play()



