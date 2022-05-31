#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: May 2022
# This program uses a 2D array

import random


def sum_of_numbers(passed_in_2D_list):
    # this function adds up all the elements in  a 2D array

    total = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element

    average = total / (len(passed_in_2D_list) * len(row_value))
    return average


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    str_rows = input("How many row would you like: ")
    str_columns = input("\nHow many columns would you like: ")

    # process & output
    try:
        int_rows = int(str_rows)
        int_columns = int(str_columns)
        for loop_counter_rows in range(0, int_rows):
            temp_column = []
            for loop_counter_columns in range(0, int_columns):
                a_random_number = random.randint(0, 50)
                temp_column.append(a_random_number)
                print("{0} ".format(a_random_number), end="")
            a_2d_list.append(temp_column)
            print("")

        average = sum_of_numbers(a_2d_list)
        print("\nThe average of all the numbers is: {0:,.2f}".format(average))
    except Exception:
        print("\nInvalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
