###Print 연습하기
print('What is your name?')  # ask for their name
MyName = input()
print('It is good to meet you, ' + MyName)
print('The length of your name is :')
print(len(MyName))
print('What is your age?')
MyAge = input()
print('You will be ' + str(int(MyAge) + 1) + ' in a year')

###while 문 만들기
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

###break 문 만들기
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

###continue 문 만들기
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')

###  0은 False이다 빈칸''도 False이다
name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
num0fGuests = int(input())
if num0fGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')

### For 루프와 range() 함수 연습하기

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

### import 연습하기
import random, sys, os, math

from random import *

### from 을 쓰면 random.을 안붙여도 된다.

for i in range(5):
    print(randint(1, 10))

import sys

while True:
    print('type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')


##함수 만들기
def hello():
    print('what is your name?')
    name = input()
    print('Hello ' + str(name))


hello()


def spam(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Error')


print(spam(2))
print(spam(0))
print(spam(33))

## this is a guess the number game
from random import *

secretnumber = randint(1, 20)
print("I' am thinking of a number between 1 to 20")
print('Correct the answer in six times')
for guesstaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretnumber:
        print('your guess is low.')
    elif guess > secretnumber:
        print('your guess is high')
    else:
        break  # this condition is the correct guess!

if guess == secretnumber:
    print('Good job! You guessed my number in ' + str(guesstaken) + ' guesses!')
else:
    print('Nope. The number i was thinking of was ' + str(secretnumber))

##collatz 수열 만들기
print('Please Enter number:')
number = input()
print(type(int(number)))
while True:
    if str(type(int(number))) == "<class 'int'>":
        print('Good')
        continue
print('please input the integer')


###다시 collatz 수열 만들기
def collatz(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            print(int(num))
        else:
            num = num * 3 + 1
            print(int(num))
        answer = answer + 1
    return (answer)


print('Please input the number')
num = input()


def is_integer(x):
    try:
        return int(x)

    except ValueError:
        print('Please input the integer')


print('the number of cycle is ' + str(collatz(is_integer(num))))

### 무엇을 더 할 수 있을까