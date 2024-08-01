"""
Exercise: Calculate the Volume of a Cylinder

Given a cylinder with a base radius `r` and height `h`, calculate its volume using arithmetic operators.

Step 1: Define variables `r` and `h` with the values of the base radius and cylinder height, respectively.
Step 2: Use the power operator (`**`) to square the radius and then multiply by the height and the value of π (pi) to
        calculate the cylinder's volume.
Step 3: Print the result of the volume calculation.

Try calculating the volume of a cylinder and verify if you get the correct result!
"""

import math

pi = math.pi
r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))

volume = pi * r**2 * h
print(f"The volume of the cylinder is: {volume}")
