import random
import sys

def main():
    # Get a random word.
    answer = getRandomWord()

    # PUT YOUR CODE HERE.
    # Start by asking the user for their initial guess
    # Ask them to "Enter a 5 letter guess?"
    # Start with section 3 in the starter doc.

    attempts = 0
    guess = ''    
    while attempts < 6 and guess != answer:
        guess = input('Enter a 5 letter guess?\n')
        printGuessColors(guess, answer)
        attempts = attempts + 1

    if guess == answer:
        print('You Won! That took ' + str(attempts) + ' guess(es).')
    else:
        print('You lost. The answer was ' + answer + '.')

def printGuessColors(guess, answer):
    for i in range(len(guess)):
        color = letterColor(i, guess, answer)
        print (guess[i] + ' - ' + color )

def letterColor(index, guess, answer):
    if guess[index] == answer[index]:
        return 'Green'
    elif guess[index] not in answer:
        return 'Red'
    else:
        return 'Yellow'


    





# A method that gets a random word from a file.
# You should not change this function.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


main()
