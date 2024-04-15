


s_1 = "III"
# Output: 3


s_2 = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

s_3 = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def rim(s):
    
    slov = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    
    res = 0
    pred = 0

    for i in s:

        if slov[i] > pred:
            res += slov[i] - 2 * pred
        else:
            res += slov[i]
        pred = slov[i]
    return res

print(rim(s_1))
print(rim(s_2))
print(rim(s_3))