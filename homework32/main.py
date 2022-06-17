import random

possible_letters = "abcdefghijklmnopqrstuvwxyz"
letter = random.choice(possible_letters)


guesses = 0
print("Your possible guesses are: %s" % possible_letters)
while 1:
    guesses += 1
    guess = input("Guess a letter: ")
    if len(guess) > 1 or guess == "":
        print("Oops. You've encountered an error! Please try again.")
        continue
    if letter == guess:
        print("Nice! You got the letter right!")
        print("You got the letter on your %dth try." % guesses)
        break
    elif letter != guess:
        print("Oops. You got the letter wrong. You have guessed %d times." % guesses)
        if guess > letter:
            print("By the way, your guess was higher in the order in the alphabet than the answer.")
        else:
            print("By the way, your guess was lower in the order in the alphabet than the answer.")


exit(0)