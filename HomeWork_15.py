import math

def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


some_variable = calculateDistance(5, 4, 8, 9)

print(some_variable)