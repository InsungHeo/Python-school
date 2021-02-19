#2020010728_허인성
#3주차_연습문제3번
import random as r

print('Hello! My name is Alice.')
print('What is your name?')
myName = input()
realDay = r.randint(1,30)
print('Well, ' + myName + 'guess my birthday from 1 to 30.')

guessDay = int(input())
if guessDay != realDay:
    print('Your guess is wrong.')
else :
    print('Excellent! ' + myName + 'You guessed my birthday.')
