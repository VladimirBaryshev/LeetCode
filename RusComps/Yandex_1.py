from typing import defaultdict


def f(s):

    if len(s) == 0:
        return []

    d = defaultdict(list)
    substr = s[0]

    for i in range(1, len(s)):
        if substr[-1] != s[i]:
            d[substr[-1]].append(len(substr))
            substr = s[i]
        else:
            substr += s[i]
    d[substr[-1]].append(len(substr))

    return [(k, max(v)) for k,v in d.items()]

# ВЕРНУТЬ САМУЮ ДЛИННУЮ ПОСЛЕДОВАТЕЛЬНОСТЬ ДЛЯ КАЖДОЙ БУКВЫ
t1 = "aabaaafcfff" # [('a', 3), ('b', 1), ('f', 3), ('c', 1)]
t2 = "a" # [('a', 1)]
t3 = "aa" # [('a', 2)]
t4 = "" # []

print(f(t1)) 
print(f(t2))
print(f(t3))
print(f(t4))