# 2002. Maximum Product of the Length of Two Palindromic Subsequences


class Solution:

    def maxProduct(self, s: str) -> int:
        N = len(s)
        d = dict()

        for mask in range(1, 2**N):
            subseq = ""
            for i in range(N):
                print(mask, i, bin(mask), bin(i), bin(1<<i))
                if mask & (1<<i):
                    print("if", mask, 1<<i, bin(mask), bin(1<<i), bin(mask & (1<<i)))
                    subseq += s[i]
        #     if subseq == subseq[::-1]:
        #         # print(subseq)        
        #         d[mask] = [len(subseq), bin(mask), subseq]

        # for m1 in d.items():
        #     for m2 in d.items():
        #         if m1[0] & m2[0] == 0:
        #             print(m1,m2)


s_1 = "leetcodecom"
# Output: 9
# Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
# The product of their lengths is: 3 * 3 = 9.

s_2 = "bb"
# Output: 1
# Explanation: An optimal solution is to choose "b" (the first character) 
# for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
# The product of their lengths is: 1 * 1 = 1.

s_3 = "accbcaxxcxx"
# Output: 25
# Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
# The product of their lengths is: 5 * 5 = 25.      


# print(Solution().maxProduct(s_1))
print(Solution().maxProduct(s_2))
# print(Solution().maxProduct(s_3))
