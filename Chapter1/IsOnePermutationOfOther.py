# Is One Permutation Of Other
# In O(n) : AAG

def isOnePermutationOfOther(s1, s2): 
    '''To Check If One String IS Permutation Of Other in range of a-z'''
    a = [0]*26
    b = [0]*26
    for i in s1: a[ord(i)-97]+=1
    for i in s2: b[ord(i)-97]+=1
    return bool(a==b)

if __name__=='__main__':
    s1,s2 = input().split()
    ans = isOnePermutationOfOther(s1, s2)
    print(ans)
    

''' Output
abcd cbda
True
'''
