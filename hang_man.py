 #we gotta add pics



#actual game code starts here
def main():
    import getpass
    print('LETS PLAY A SIMPLE GAME OF HANGMAN')
    print('YOU HAVE 8 CHANCES SO.... GOTTA BE CAREFUL')
    #secret_word = input('PLAYER ONE SHOULD ENTER A WORD: \n')
    #print('\n'* 20)
    #return secret_word


    #now we will split the word and create a list called list_
    list_ = list(secret_word)
    number_of_letters = len(list_)


    #now we create an empty list to hold all the values the second user enters if they correct
    x = []
    for n in range(number_of_letters):
        n = '_'
        x.append(n)
    print(x)


    # preconditions before the second user starts to enter guesses
    guess_counter = 0
    guess_limit = 8
    out_of_chances = False
    correct_guess = False

    #the second user starts to enter there guesses
    while guess_limit != guess_counter and not(out_of_chances) and not(correct_guess):
        if guess_counter <= guess_limit and x != list_:
            try:
                guess = input('Which letter do you think is in the word')
                guess_counter += 1
            except:
                print('madddd')


            if guess in secret_word:
                print(f'this is trial number: {guess_counter}')
                print('CORRECT!!! letter in the word')
                position = list_.index(guess)
                x[position] = guess
                print(x)
                #if x = list_:
                    #print('____YOU WIN!!!!!!!!!!!!____')





            else:
                if guess_counter < 9 and x != list_:
                    print(f'this is trial number: {guess_counter}')
                    print('OOPS try again')
                    print(x)

        else:
            if x == list_:
                correct_guess = True
                print('____YOU WIN!!!!!!!!!!!!____')
                exit()
            elif guess_counter > 8 and x != list_:
                print('OUTTA MOVES')

    #the hang man images
                    #def hangman():

                    #if guess_counter == 1 and not(guess in secret_word):
                        #print(0)
                    #elif guess_counter == 2 and not(guess in secret_word):
                        #print()

        #except:print("out of chances")



    else:
        print('OUT OF MOVES..BUT DON\'T WORRY YOU COULD CONTINUE ANYWAY')
        again = input('Do you want to try  again\n enter 1 to start the again: \n')
        if again == '1':
            print('SECOND TRIAL')
            main()
        else:
            exit()

        print('..................................................................................................')
secret_word = input('PLAYER ONE SHOULD ENTER A WORD: \n')
print('\n'* 120)
main()

