count = 0

def isPalindrome(s, l, r):
    global count
    while (l >= 0 and r < len(s) and s[l] == s[r]):
        count += 1
        l -= 1
        r += 1

def countPalindromes(s):
    global count
    count = 0
    for i in range(len(s)):
        isPalindrome(s, i, i)
        isPalindrome(s, i, i + 1)
    
    return count

s = input()
n = int(input())
strings = []
for i in range(n):
    [l, r] = input().split()
    l = int(l)
    r = int(r)
    
    print(countPalindromes(s[l-1:r]))