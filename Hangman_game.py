import random

class HangmanGame():

    game_win = 0
    game_lost = 0

    def __init__(self):

        self.word_list = ['zebra', 'chicken', 'apple', 'oregano', 'hippopotamus', 'alignment', 'python', 'terminal', 'jovial', 'technology', 'git', 'album']
        print "Previous Game Stats: "+"\nGames Won: "+str(HangmanGame.game_win)+"\nGames Lost: "+str(HangmanGame.game_lost)
        new_game = raw_input("Would you like to start a new game?...(Y/N)")
        if new_game == 'Y':
            self.start_game()
        elif new_game == 'N':
            print ":("
            exit()
        else:
            print 'Sorry, please enter either Y or N'
            self.__init__()

    def start_game(self):

        previously_guessed = []
        wrong_guess = 0
        n = 0

        word = random.choice(self.word_list)
        hidden_word = len(word) * "_ "
        hiddenWordList = list(len(word)*'_')
        print hidden_word

        while n != len(list(word)):

            letter_guess = raw_input("Pick 1 letter...")
            lower_case_letter = letter_guess.lower()
            if len(list(lower_case_letter)) > 1 or lower_case_letter == " " or lower_case_letter == "":
                print "Sorry, that's not a valid guess!"
                letter_guess = raw_input("Pick 1 letter...")
                lower_case_letter = letter_guess.lower()

            if lower_case_letter in previously_guessed:
                print "You've already guessed that before..."
                letter_guess = raw_input("Pick 1 letter...")
                lower_case_letter = letter_guess.lower()
            else:
                previously_guessed.append(lower_case_letter)
                
            indexList = []
            wordArray = list(word)

            for i in range(len(wordArray)):
                if wordArray[i] == lower_case_letter:
                    indexList.append(i)
                
            if len(indexList) > 0:
                for i in indexList:
                    hiddenWordList.pop(i)
                    n += 1
                    hiddenWordList.insert(i, lower_case_letter)
                self.hangman(wrong_guess, word)
                reqString = ''.join(hiddenWordList)
                print reqString
                if reqString == word:
                    print "Congratulations, you won the game!"
                    HangmanGame.game_win += 1
                    self.__init__()
            else:
                print "Whoops, wrong guess!"
                wrong_guess += 1
                print "Number of wrong guesses: "+str(wrong_guess)
                self.hangman(wrong_guess, word)

    def hangman(self, wrong_guess, word):
        
        if wrong_guess == 0:
            print "________      "
            print "|      |      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
            print "|________     "
            
        elif wrong_guess == 1:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|             "
            print "|             "
            print "|             "
            print "|________     "

        elif wrong_guess == 2:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|     /       "
            print "|             "
            print "|             "
            print "|________     "

        elif wrong_guess == 3:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|     /|      "
            print "|             "
            print "|             "
            print "|________     "

        elif wrong_guess == 4:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|     /|\     "
            print "|             "
            print "|             "
            print "|________     "

        elif wrong_guess == 5:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|     /|\     "
            print "|     /       "
            print "|             " 
            print "|________     "

        else:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|     /|\     "
            print "|     / \     "
            print "|             "
            print "|________     "
            print "Game Over! The correct word was "+str(word)
            HangmanGame.game_lost += 1
            self.__init__()

game = HangmanGame()