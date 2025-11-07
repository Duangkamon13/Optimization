"""
A digital image is composed of multiple pixels.
Each pixel has 3 color channels: red, green, and blue, or R, G, B for short.
The brightness of a pixel is a combined effect from 3 color channels
and can be calculated from: Y = 0.2126R + 0.7152G + 0.0722B,
where Y is the brightness, often called relative luminance.
Write a program to take in color channels and calculate
and print out the corresponding relative luminance.
"""

R = int(input('R Channel[0-255]:'))
G = int(input('G Channel[0-255]:'))
B = int(input('B Channel[0-255]:'))

Y = 0.2126*R+ 0.7152*G + 0.0722*B

# Do not edit below this line
# ---------------------------------

print("Y = %d" % (Y))


