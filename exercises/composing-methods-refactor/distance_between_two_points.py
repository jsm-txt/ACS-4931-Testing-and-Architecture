# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math
xc1 = 4
yc1 = 4.25
xc2 = 53
yc2 = -5.35
# Calculate the distance between the two circle
def distance_between_two_cicles(x1, y1, x2, y2):
  print('distance', math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2))
# *** somewhere else in your program ***
xa = -36
ya = 97
xb = .34
yb = .91
# calcualte the length of vector AB vector which is a vector between A and B points.
def length_of_ab_vector(xa, xb, ya, yb):
  print('length', math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb)))
