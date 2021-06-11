#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: June 11, 2021
# The program places the numbers into a single variable
# and prints them to the console. The program has a function
# to find the maximum value of a list.

import random


def find_max_value(list_of_numbers):

    maximum = -1
    for counter in range(0, len(list_of_numbers)):
        if(list_of_numbers[counter] > maximum):
            maximum = list_of_numbers[counter]
    return maximum


def main():
    # this function uses an array
    list_of_int = []
    max_value = 0

    # input
    for loop_counter in range(0, 10):
        random_num = random.randint(10, 100)
        list_of_int.append(random_num)
    print("")

    for loop_counter in range(0, 10):
        print("{} added to the list at position"
              " {} ".format(list_of_int[loop_counter], loop_counter))
    print("")
    # gets the maximum value from the list and displays it
    max_value = find_max_value(list_of_int)
    print("The max value is: {}". format(max_value))


if __name__ == "__main__":
    main()
