import math

figType = input()

if figType == "square":
    a = float(input())
    area = a * a
    print("%.3f" % area)
elif figType == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print("%.3f" % area)
elif figType == "circle":
    r = float(input())
    area = math.pi * r * r
    print("%.3f" % area)
elif figType == "triangle":
    a = float(input())
    ha = float(input())
    area = a * ha / 2
    print("%.3f" % area)
