# Is Rotated String From One Call Of Is Substring
# O(n): AAG

def IsRotated(s1, s2): 
    '''To Check Is Rotated String From One Call Of Is Substring '''
    return len(s1)==len(s2) and s2 in s1+s1
                            
if __name__=='__main__':
    s1,s2 = input().split()
    ans = IsRotated(s1, s2)
    print(ans)
    

''' Output
waterbottle erbottlewat
True
'''
