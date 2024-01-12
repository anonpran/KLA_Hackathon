import math
import numpy as np
#import matplotlib.pyplot as plt


def milestone1(d,n,a):

    #using the angle calculting the line wrt to centre
    radius = d/2
    #print(radius)
    
    res=[]
    for i in range(n):

        xi = radius*math.cos(a+(2*math.pi*i)/n)
    #print(math.cos(0))
    #print(xi)
        yi = radius*math.sin(a+(2*math.pi*i)/n)
        res.append([round(xi,4),round(yi)])

    #print(yi)
    print(res)

    import numpy as np
    x = np.linspace(-150,150)
    #now x is the line with equidistant points



    with open("21pc19.txt","w") as f:
        for i in range(len(res)):
            print(res[i])
            #f.write("("+"res[i]"+")")
            #f.write(','.join(str(res[i])))
            temp =str(res[i]).strip('[')
            temp = str(temp.strip(']'))
            f.write("("+temp+")")
            f.write("\n")
""""
    circles=[]
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = radius * np.cos(t)
    y = radius * np.sin(t)
    circles.append(np.c_[x, y])
    print(circles)
    res=[]
    for i in range(n):
        temp = radius*(math.exp(i*2*math.pi*)
        res.append(temp)
    
    s = len(a)
    lo = 360./(s + n)
    hi = 2. * lo
    d = (lo + hi)/2
    c = sum(floor(x/d) for x in a)
    while c != (n + s):
        if c < (n + s):
            hi = mid
        else:
            lo = mid
        d = (lo + hi)/2
        c = sum(floor(x/d) for x in a)
    print(d)

    #spherical_data = np.zeros_like(data)
    #for i,d in enumerate(data):
    r = math.sqrt(radius**2 + d[1]**2 + d[2]**2)
    theta = math.acos(d[2] / r)
    phi = math.atan(d[1] / d[0])

        spherical_data[i] = np.array([r, theta, phi])

    return spherical_data"""
"""
    line_length = d
    if a==0:
        final = np.linspace(-radius,radius,n)
    #print(final)
        with open("21pc19.txt","w") as f:
            for i in range(len(final)):
                temp = "("+str(final[i])+","+"0" +")"
                f.write(temp)
                f.write("\n")

        if a==180:
            final = np.linspace(-radius,radius,n)
    #print(final)
        with open("21pc19.txt","w") as f:
            for i in range(len(final)):
                temp = "("+"0"+","+str(final[i]) +")"
                f.write(temp)
                f.write("\n")

        

        if a==180:
            final = np.linspace(-radius,radius,n)
    #print(final)
        with open("21pc19.txt","w") as f:
            for i in range(len(final)):
                temp = "("+f'(i+(2/3))'+","+str(final[i]) +")"
                f.write(temp)
                f.write("\n")
        
    a = Point(0, 0)
    b = Point(0, 0)
    m = math.tan(a)
    # slope is 0
    if m == 0:
        a.x = source.x + l
        a.y = source.y
 
        b.x = source.x - l
        b.y = source.y
 
    # if slope is infinite
    elif math.isfinite(m) is False:
        a.x = source.x
        a.y = source.y + l
 
        b.x = source.x
        b.y = source.y - l
    else:
        dx = (l / math.sqrt(1 + (m * m)))
        dy = m * dx
        a.x = source.x + dx
        a.y = source.y + dy
        b.x = source.x - dx
        b.y = source.y - dy
 


    
    import math

def rotate(origin, point, angle):
    
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    
    ox, oy = 0,0
    px, py = res[0],res[1]
    

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy
"""

    
    




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




