import random


possible_letters = "abcdefghijklmnopqrstuvwxyz"
print("What level do you want to choose?")
print("Levels: \n\t-Baby (100 guesses)\n\t-Easy (15 guesses)\n\t-Average (10 guesses)\n\t-Hard (6 guesses)\n\t-Impossible (3 guesses)")
print("Choices: \n\t-1 (Baby) \n\t-2 (Easy)\n\t-3 (Average)\n\t-4 (Hard)\n\t-5 (Impossible)")

level = input("Please choose a level: ")

letters = [random.choice(possible_letters), random.choice(possible_letters), random.choice(possible_letters)]

guess_count = {
    '1': 100,
    '2': 15,
    '3': 10,
    '4': 6,
    '5': 3
}

guesses = guess_count[level]
used_guesses = 0
guessed_letters = 0
flag = False
def game():
    global used_guesses, guesses, guessed_letters, flag
    for guessf in letters:
        while 1:
            used_guesses += 1
            guess = input("Please guess your letter: ")
            if guess == guessf:
                guessed_letters += 1
                print("Congrats! You have guessed %d of the 3 letters." % guessed_letters)
                break
            elif guess != guessf:
                print("Oops. Your letter is not one of the three letters.")
                print("You have %d guesses left." % (int(guesses) - int(used_guesses)))
                if guess > guessf:
                    print("Your guess was higher in the order in the alphabet than the letter.")
                    continue
                elif guess < guessf:
                    print("Your guess was lower in the order in the alphabet than the letter.")
                    continue
            if used_guesses == guesses or used_guesses <= 0:
                print("GAME OVER. You used all of your guesses.")
                print("The letters were {}.".format(print(i) for i in letters))
                flag = True
                break
        if flag:
            break
    if guessed_letters == 3:
        print("Congrats! You have guessed all the letters!!!")
        exit(0)

game()