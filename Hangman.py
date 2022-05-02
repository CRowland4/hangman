import random


def give_menu():
    print("H A N G M A N")
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        return play_game()
    elif choice == 'exit':
        pass
    else:
        return give_menu()


def play_game():
    word_bank = ['python', 'java', 'kotlin', 'javascript']
    guesses = []
    answer = random.choice(word_bank)
    hidden_word = ['-' for letter in answer]
    win = False
    tries = 8
    while tries > 0:
        if '-' not in hidden_word:
            win = True
            break
        else:
            pass

        print('\n' + ''.join(hidden_word))
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print("You should input a single letter")
            continue
        elif not (guess.isalpha() and guess.islower()):
            print("Please enter a lowercase English letter")
            continue
        elif guess in guesses:
            print("You've already guessed this letter")
            continue
        elif guess not in answer:
            print("That letter doesn't appear in the word")
            guesses.append(guess)
            tries -= 1
            continue
        elif guess in answer:
            guesses.append(guess)
            for i in range(len(answer)):
                if guess == answer[i]:
                    hidden_word[i] = guess
                else:
                    continue

    if win:
        print(f'{answer}\nYou guessed the word!\nYou survived!\n')
        return give_menu()
    else:
        print('You lost!\n')
        return give_menu()

give_menu()
