import random as r

#build the word from guessed_letters with their correct positions
def buildword():
    guessed_word = ''
    pos_value = 1
    attempts = len(word)
    while pos_value <= attempts:
        for char in guessed_letters.keys():
            if pos_value == guessed_letters[char]:
                guessed_word = guessed_word + char + ' '
                break
        pos_value = pos_value + 1
    return guessed_word

def comparewords(guessed_word):
    print("the word you guessed is:")
    # compare real word to guessed_word stripped off spaces.
    if word == guessed_word.replace(' ', ''):
        print(guessed_word)
        print("You won!!")
    else:
        print(guessed_word)
        print("Sorry, You lost!")


# while loop
# if else's
# user input
# random word generator from a fake dictionary

# generate random words
words = ["road", "baby", "head", "hand"]
word = words[r.randint(0,3)]
print(word)

# number of guesses to track
attempts = 0

#this is a dictionary to track letters and their position.
guessed_letters = {}
# user gets four attempts since we picked four letter word from dictionary
while attempts < 4:
    ch = input("guess a letter in 4 letter word: ")
    index = None
    # check if character guessed (input via terminal) is in the word
    if ch in word:
        # this loop will track and store the character and their position in the word
        for i in range(0, len(word)): 
            if word[i] == ch: 
                index = i + 1
                guessed_letters[ch] = index
                break

        #display of guessed word
        for i in range(0, len(word)):
                if i + 1 == index:
                    # trying to print the characters previously guessed together.
                    temp_word = buildword()
                    print(ch + " ", end="")
                else:
                    print("_ ", end="")
        print()
    attempts = attempts + 1

guessed_word = buildword()
comparewords(guessed_word)
