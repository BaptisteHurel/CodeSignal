#ex1
def add(param1, param2):
    return param1+param2;
 
param1 = 1
param2 = 2

add(param1, param2)

#-----------------------------------------
#ex2
def centuryFromYear(year):
    if year % 100 == 0:
        return year/100
    else:
        return int(year/100) + 1
    
#-----------------------------------------
#ex3
def checkPalindrome(s):
    return s == s[::-1]
 
 
s = "aabaa"
ans = checkPalindrome(s)
 
if ans:
    print("Palindrome")
else:
    print("Not Palindrome")
 
