# Urlify 
# In O(n) : AAG

def Urlify(s): 
    '''To Urlify a string Replacing Spaces with %20'''
    return s.strip().replace(' ','%20')


if __name__=='__main__':
    ans = Urlify(input("Enter String to Urlify: "))
    print(ans)
    

''' Output
Enter String to Urlify: Mr John Smith   
Mr%20John%20Smith
'''
