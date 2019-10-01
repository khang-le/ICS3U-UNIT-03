#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program checks if there is over 30 students

import constants


def main():
    # this function checks if there is over 30 students

    # input
    number_of_students = int(input("Enter the number of studetns: "))
    print("")

    # process and output
    if number_of_students == constants.MAX_STUDENT_NUMBER1:
        print("EXACTLY 30 STUDENTS!")
    else:
        print("Not 30 students!")


if __name__ == "__main__":
    main()
