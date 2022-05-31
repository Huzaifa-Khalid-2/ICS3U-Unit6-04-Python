#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: May 2022
# This program print 10 random numbers and shows the largest number

import random


def largest_number(number):
    # This function finds the largest number

    big_number = number[1]

    # process
    for counter in number:
        if counter > big_number:
            big_number = counter

    return big_number


def main():
    # This function prints the largest number
    number = []

    # heading
    print("A list of random numbers: ")
    print("")

    # process
    for counter in range(1, 11):
        random_numbers = random.randint(1, 100)
        number.append(random_numbers)
        print("The random number is {0}".format(random_numbers))

    # call functions
    big_number = largest_number(number)

    # output
    print("\nThe largest number is: {0}".format(big_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
