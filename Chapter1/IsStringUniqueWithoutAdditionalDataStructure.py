# Is String Unique Without AdditionalDataStructure
# In O(nlogn) : AAG

def isSrtingUnique(data):
    '''To Check If String IS Unique Any Without AdditionalDataStructure'''
    data = sorted(data)
    for i in range(len(data)-1):    
        if data[i]==data[i+1]:
            return False
    return True

if __name__=='__main__':
    data = input()
    ans = isSrtingUnique(data)
    print(ans)
    

