import math
import numpy as np
#import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R


def milestone1(d,n,a):

    #using the angle calculting the line wrt to centre
    radius = d/2
    #print(radius)


    # Calculate the radius based on the given diameter
    radius = d / 2

    # Generate equidistant points on the x-axis
    num_points = n
    theta_degrees = a
    x_points = np.linspace(-radius, radius, num_points)

    # Rotate points by the given angle (theta) in degrees
    theta_radians = np.radians(theta_degrees)
    x_rotated = x_points * np.cos(theta_radians) - np.zeros_like(x_points) * np.sin(theta_radians)
    y_rotated = x_points * np.sin(theta_radians) + np.zeros_like(x_points) * np.cos(theta_radians)
    

    #print(x_rotated, y_rotated)
    

    with open("21pc19_4.txt","w") as f:
        for i in range(len(x_rotated)):
            #print(res[i])
            #f.write("("+"res[i]"+")")
            #f.write(','.join(str(res[i])))
            tempx =str(round(x_rotated[i],4)).strip('[')
            tempy = str(str(round(y_rotated[i],4)).strip(']'))
            f.write("("+tempx+","+tempy+")")
            f.write("\n")

#Opening the file
try:
    arr=[]
    filename = input()
    f = open(filename,'r')
    #print(f.read())
    #print(f.readline())
    arr.append(f.readline().split(':'))
    arr.append(f.readline().split(':'))
    arr.append(f.readline().split(':'))
    inp = []
    for i in range(len(arr)):
        inp.append(int(arr[i][1].strip()))
    #print(inp)

    wafer_diameter = inp[0]
    number = inp[1]
    angle=inp[2]
    #print(wafer_diameter)
    #print(number)
    #print(angle)

    milestone1(wafer_diameter,number,angle)


except IOError:
    print("Error taking the input")
#print(arr[0])
