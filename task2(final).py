def milestone2(diameter,size,shift,dow):

    #Step 1:
    #given the centre(0,0) now will have to move towards that cell
    #shfit vector is pointing towards
    x, y = 0,0
    
    #result is the string that will hold the final output
    res=""
    result = []
    origin = (x,y)
    try:
        x_new = x + x_new
        y_new = y + y_new

    except IOError:
        print("Error moving")

    #Step 2:
    #Fixing the reference point given as index (0,0)
    try:
        #calculating the reference using the distacne from COW and COW(0,0)
        reference_x = (dow[0]-0)
        reference_y = (dow[1]-0)
        new_origin_x = reference_x
        new_origin_y = reference_y

    except Exception as e:
        print("Indexing error",e)
        
    
    #Step 3: 
    #Implementing a dfs search algorithm to search for all valid cells
    def dfs(i,j,r,c,diameter):
        #to hold the locations that has already been visisted
        seen=[]
        r = diameter /2
        c = diameter / 2
        #rx and ry are reference coordinates and checking all boundary conditions
        if i > r or j > c or i < (-diameter) or j < (-diameter):
            return 0
        
        #to remove recursive calling problem
        seen.append([i,j])
        #else keep calling a dfs method to move in all possible directions
        #horizontal and vertical
        dfs(i-1,j,r,c,diameter)
        dfs(i+1,j,r,c,diameter)
        dfs(i,j-1,r,c,diameter)
        dfs(i,j+1,r,c,diameter)

    res = dfs(new_origin_x,new_origin_y,r,c,diameter)

    res+= "("+"new_origin_x"+")"+":"+"("+i+","+y+")"
    result.append(res)
    return res

#Opening the file
try:
    arr=[]
    filename = input()
    f = open(filename,'r')
    arr.append(f.readline().split(':'))
    arr.append(f.readline().split(':'))
    arr.append(f.readline().split(':'))
    arr.append(f.readline().split(':'))
    inp = []
    for i in range(len(arr)):
        inp.append(int(arr[i][1].strip()))

    wafer_diameter = inp[0]
    size = inp[1]
    shift=inp[2].split()
    dow = inp[3].split()

    

    milestone2(wafer_diameter,size,shift,dow)


except IOError:
    print("Error taking the input")
