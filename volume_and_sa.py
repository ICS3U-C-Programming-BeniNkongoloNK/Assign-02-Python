#!/usr/bin/env python3
# Created By: Beni
# Date: February 28 2025
# A program to calculate the volume and lateral surface area of a square-based pyramid

# Imports a time and system(sys) function
import time
import sys
import math


# Defines a 'write' function that makes strings show up letter by letter
def write(str, eol="\n"):
    for char in str:
        time.sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write(eol)
    sys.stdout.flush()
    return ""


# Defines main
def main():

    # Introduction and explanation as to what to do
    write("Hello, I am a calculator")
    write(
        "I am going to calculate stuff frfr. But only for a square-based pyramid cuz im dumb fr"
    )

    # Decides if you're working with volume or lateral surface area
    write(
        "Do you want to calculate the volume or the surface area (v=volume; a= lateral surface area):  "
    )
    calculate = input("")
    input_again = 3

    # If you did not input 'v' or 'a' a loop starts making you repeat the input. If you fail 3 times the program ends
    while calculate not in ["v", "a"]:
        input_again = input_again - 1
        if input_again == 0:
            write(
                "Clearly you're dumber than me, and i'm the dumb calculator. So u don't get to use me"
            )
            break

        write("Thats not a valid input, try again")
        calculate = input("")
        ()

    # If the person wants to calculate the volume
    if calculate == "v":
        write("What is the base edge?: ")
        base_edge = float(input())
        write("Thank you. Now, what is the height of your pyramid")
        height = float(input())
        write("The volume of your square-based pyramid is: ")
        print((base_edge**2) * height / 3)

    # If the person wants to calculate the lateral surface area
    if calculate == "a":
        write("What is the base edge?: ")
        base_edge = float(input())
        write("Thank you. Now, what is the height of your pyramid")
        height = float(input())
        write("The lateral surface or something of your square-based pyramid is: ")
        print(("{}".format(base_edge * (math.sqrt(base_edge**2 + 4 * height**2)))))


if __name__ == "__main__":
    main()
