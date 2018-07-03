# String Compression
# O(n) : AAG

def StringCompression(data):
    '''To Compress String'''
    size = len(data)
    compressed = []
    i=0
    while i<size:
        value = data[i]
        count=0
        while i<size and data[i]==value:
            count+=1
            i+=1
        compressed.append(value+str(count))
    return data if len(compressed)>=size else "".join(compressed) 


if __name__=='__main__':
    data = input()
    ans = StringCompression(data)
    print(ans)
    
''' Output
aabcccccaaa
a2b1c5a3
'''
