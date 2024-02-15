# Welcome to my perfect Guess

Welcome to a simple guessing game where you try to guess a random number between 1 and 1000!

## How to Play

1. You will be prompted to guess a number.
2. Keep guessing until you get it right or decide to quit by entering '0'.
3. After each guess, the game will give you hints to help you get closer to the correct number.

## Hints

- If your guess is within 100 of the correct number, you'll be told you're "too close".
- If your guess is less than half of the correct number, you'll be told to go higher.
- If your guess is more than double the correct number, you'll be told to go lower.
- Otherwise, you'll receive generic hints to guide you.

## Exiting the Game

To exit the game, simply enter '0'. The correct number will be revealed, and you'll lose the game.

## Example

Guess:
300
You are too close
Hint: There is a difference of 200 greater or lesser

Guess:
700
You are too Close
Try it again!
Hint: Make it higher

Guess:
500
Not close
Try it again!
Hint: A little bit lower

Guess:
200
Soo far!
Try it again!
Hint: make it lower

Guess:
350
Far...!
Try again!
Hint: Make it higher

Guess:
400
You Won
I can't believe you did it!
Actual number is {num}