import math
import numpy as np
from scipy.spatial.transform import Rotation as R


def milestone1(d,n,a):
    try:
        radius = d/2
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
                tempx =str(round(x_rotated[i],4)).strip('[')
                tempy = str(str(round(y_rotated[i],4)).strip(']'))
                f.write("("+tempx+","+tempy+")")
                f.write("\n")
    except Exception as e:
        print("The error is: ",e)

#Opening the file
try:
    arr=[]
    filename = input()
    f = open(filename,'r')
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

    milestone1(wafer_diameter,number,angle)
except IOError:
    print("Error taking the input")
