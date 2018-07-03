# Rotate Matrix By 90 Degree
# :AAG

def TransposeMatrix(size, data):
    ''' To Inplace Transpose Matrix '''
    for i in range(size):
        for j in range(i+1,size):
            data[i][j],data[j][i] = data[j][i],data[i][j]
    return data

def RotateMatrixBy90Degree(size, data): 
    '''To Rotate Matrix By 90 Degree'''
    for i in range(size//2):
        data[i],data[size-i-1]=data[size-i-1],data[i]
    data = TransposeMatrix(size, data)
    return data


if __name__=='__main__':
    size = int(input("Enter Size: "))    
    data = [ list(map(int, input().split())) for i in range(size) ]
    ans = RotateMatrixBy90Degree(size, data)
    print('-----')
    for line in ans:      
        print(*line)
    

''' Output
Enter Size: 3
1 2 3
4 5 6
7 8 9
-----
7 4 1
8 5 2
9 6 3
'''
