def palindrome(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return palindrome(s,l+1,r-1)

input="nitin"
length=len(input)-1
print(palindrome(input,0,length))