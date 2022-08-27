#!/usr/bin/python3

def print_last_digit(number):
    LDigit = abs(number) % 10
    print(f"{LDigit:d}", end='')
    return LDigit
