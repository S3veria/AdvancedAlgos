def oddString(s):
    newS = "#"
    for c in s:
        newS += c + "#"
    return newS

def oddPalindromes(s):
    n = len(s)
    l = 0
    r = -1
    oddP = [0 for _ in range(n)]

    for i in range(n):
        if i <= r:
            oddP[i] = min(oddP[l + r - i], r - i)
        left = i - oddP[i] - 1
        right = i - oddP[i] + 1
        while left >= 0 and right < n and s[left] == s[right]:
            oddP[i] = oddP[i] + 1
            left -= 1
            right += 1
        if i + oddP[i] > r:
            l = i - oddP[i]
            r = i + oddP[i]
    return oddP

def evenPalindromes(s):
    n = len(s)
    l = 0
    r = -1
    evenP = [0 for _ in range(n)]

    for i in range(n):
        if i <= r:
            evenP[i] = min(evenP[l + r - i], r - i)
        left = i - evenP[i]
        right = i - evenP[i] + 1
        while left >= 0 and right < n and s[left] == s[right]:
            evenP[i] = evenP[i] + 1
            left -= 1
            right += 1
        if i + evenP[i] > r:
            l = i - evenP[i] + 1
            r = i + evenP[i]
    return evenP

string = "aabacab"
print(oddPalindromes(string))
print(evenPalindromes(string))

