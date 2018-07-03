# Palindromic Permutation
# In O(n) : AAG

def PalindromicPermutation(s): 
    '''To Check If It Is A Permutation of Palindrome in range a-z'''
    a = [0]*26
    for i in s.replace(" ",""): a[ord(i)-97]+=1
    odd_instances = sum([1 for i in range(26) if a[i]%2==1])  #Counting Odd Instances Of Character     
    return bool(odd_instances <=1 )

if __name__=='__main__':
    ans = PalindromicPermutation(input("Enter Here: "))
    print(ans)
    

''' Output
Enter Here: tact coa
True
'''
