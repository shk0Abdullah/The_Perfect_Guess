'''-----------------Welcome to my perfect Guess------------------'''
import random as r
import sys 
num = r.randint(1,1000)
while True: 
    try:
        guess = int(input('Guess :\n'))
        if guess == 0:
            print(f'You lose\nNumber is {num}')
            break
            sys.exit()
        if guess == num:
            print('You Won')
            print(f'I can"t believe you do it\nActual number is {num}')
            break
            sys.exit()
        elif num-guess <= 100 and num - guess >= -100:
            print('You are too close\nHint: There is a difference of 200 greater or lesser')
        elif guess < num and num/guess <= 2 :
            print('You are too Close')
            print('Try it again!')
            print('Hint: Make it higher')
        elif num/guess < 1.5:
            print ("Not close ")    
            print("Try it again!")
            print('Hint: A little bit lower')
        elif guess > num and num/guess < 0.5:
            print("Soo far!\nTry it again!\nHint: make it lower")
        elif num/guess >= 0.5:
            print('Far...!\nTry again!\nHint: Make it higher')
    except:
        pass