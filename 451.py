# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/description/


def decrising_order_(string: str) -> str:

    d = dict()
    buckets = [[]]
    result_string = ""

    for s in string:

        buckets.append([])

        if s not in d:
            d[s] = 1
        else:
            d[s] += 1


    for k,v in d.items():
        buckets[v].append(k*v)

    buckets = reversed(buckets)

    for b in buckets:
        result_string += "".join(b)

    return result_string
        


s_1 = "tree" # Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

s_2 = "cccaaa" # Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.

s_3 = "Aabb" # Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

s_4 = "eeeee" # Output: "eeeee"

s_5 = "raaeaedere" #Output:"eeeeaaarrd"

print(decrising_order_(s_1))
print(decrising_order_(s_2))
print(decrising_order_(s_3))
print(decrising_order_(s_4))
print(decrising_order_(s_5))








    