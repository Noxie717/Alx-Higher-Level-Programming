#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Num = number

if number < 0:
	number = -(number)

LDigit = number % 10
if Num < 0:
	number = Num
	LDigit = -(LDigit)

if LDigit > 5:
	string = "and is greater than 5"
elif LDigit == 0:
	string = "and is 0"
elif LDigit < 6:
	string = "and is less than 6 and not 0"

print(f"Last digit of {number:d} is {LDigit:d}", string)
