def oddString(s):
    newS = "#"
    for c in s:
        newS += c + "#"
    return newS

def manacher(s):
    #set string as #s#t#r#i#n#g#
    s = oddString(s)
    n = len(s)

    #set delimeters
    s = "$" + s + "^"
    
    p = [0 for _ in range(n + 2)]
    l = r = 1
    for i in range(1, n + 1):
        p[i] = max(0, min(r - i, p[l + (r - i)]))
        while(s[i - p[i]] == s[i + p[i]]):
            p[i] += 1
        if(i + p[i] > r):
            l = i - p[i]
            r = i + p[i]
    return p[:-2]
    

string = "aabacab"
strings = [string[:], string[:4], string[2:7], string[1:5], string[4:]]
def listToString(l):
    string = ""
    for s in l:
        string += str(s)
    return string

def count(intList):
    total = 0
    for i in range(2, len(intList), 2):
        total += intList[i]
    return total / 2

for s in strings[:]:
    man = manacher(s)
    print(listToString(man))
    print(oddString(s))
    print(count(man))