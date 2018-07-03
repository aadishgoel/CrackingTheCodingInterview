# One Away
# O(n): AAG

def OneAway(s1, s2): 
    '''To Check If One String IS One Edit Away From Another
        Where Edit Can Be: Insert, Remove Or Replace '''
    l1,l2 = len(s1),len(s2)
    if(l1==l2):
        return( sum([1 for i,j in zip(s1,s2) if i!=j]) <= 1)
    elif abs(l1-l2)==1:
        s1,s2 = (s1,s2) if l1>l2 else (s2,s1)
        count=i=j=0
        while i<len(s1) and j<len(s2):
            if s1[i]==s2[j]:
                i+=1
                j+=1
                continue
            count+=1
            i+=1
        return(count <= 1)
    return False
            
                
if __name__=='__main__':
    s1,s2 = input().split()
    ans = OneAway(s1, s2)
    print(ans)
    

''' Output
abcde abde 
True
'''
