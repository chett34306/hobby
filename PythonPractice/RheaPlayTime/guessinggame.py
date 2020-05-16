
#random number generator (1,10)
#prompt from guessor for number
#if to check guessed number is same as host number
    #else, nice try, try again,
#while loop
    #variable x = rand_numberf
#have counter for number of attempts
#import random
#check for previous numbers.



import random as rand
x = rand.randint(1,100)
previous = []
counter = 0
while True:
    y = input("Please guess a number between 1 to 100: ")
    counter = counter + 1
    if counter == 4:
        print("You lost the game you fool. All attempts are over. Good bye!")
        break
    if x == int(y):
        print ("Yay..smarty pants! you got it..go get a cookie for me")
        break
    elif x < int(y):
        if y in previous:
            print(" You have already used this number")
            counter = counter - 1
        else:
            print("Your number is higher")
    elif x > int(y):
        if y in previous:
            print(" You have already used this number")
            counter = counter - 1
        else:
            print("Your number is lower")
    previous.append(int(y))

        