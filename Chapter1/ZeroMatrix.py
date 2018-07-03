# Zero Matrix
# O(Elements in matrix) :AAG

def ZeroMatrix(size, data): 
    '''To Zero the row and column if elment is zero'''
    row = [0]*size
    column = [0]*size
    for i in range(size):
        for j in range(size):
            if not data[i][j]:
                row[i]=column[j]=1

    for i in range(size):
        if row[i]:
            data[i]=[0]*size
            continue
        for j in range(size):
            if column[j]: data[i][j]=0    
    return data


if __name__=='__main__':
    size = int(input("Enter Size: "))    
    data = [ list(map(int, input().split())) for i in range(size) ]
    ans = ZeroMatrix(size, data)
    print('-----')
    for line in ans:      
        print(*line)
    

''' Output
Enter Size: 3
0 2 3
4 5 6
7 8 0
-----
0 0 0
0 5 0
0 0 0
'''
