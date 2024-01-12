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
