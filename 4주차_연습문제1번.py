#2020010728_허인성
#4주차_연습문제1번
import random as r

print('Hello! what is your name? ')
myName = input()

number = r.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20. ')

guess = 0
guessesTaken = 0

while guessesTaken < 6:
    guessesTaken += 1

    print('Take a guess.', end = '')
    guess = int(input())

    if guess < number:
        print('Your guess is too low.\n')

    elif guess > number:
        print('Your guess is too high.\n')

    else :
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
        break

if guessesTaken == 6:
    print('You didn`t get the right answer in 6 tries.')
