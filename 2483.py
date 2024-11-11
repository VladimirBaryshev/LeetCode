# 2483. Minimum Penalty for a Shop

from collections import OrderedDict

class Solution:

    def bestClosingTime(self, customers: str) -> int:
        
        y_count = 0
        for v in customers:
            if v == "Y":
                y_count += 1

        d = OrderedDict()
        n_count = 0
        for i,v in enumerate(customers):

            if v == "Y":
                d[i] = {"Y": y_count, "N": n_count}
                y_count -= 1

            if v == "N":
                d[i] = {"Y": y_count, "N": n_count}
                n_count += 1

        d[i+1] = {"Y": y_count, "N": n_count}
        

        min_sum = (10**5)+1
        min_i = 0

        for k in d.keys():
            if (d[k]["Y"] + d[k]["N"]) < min_sum:
                min_sum = d[k]["Y"] + d[k]["N"]
                min_i = k

        return min_i
        


customers_1 = "YYNY"
# Output: 2
# Explanation: 
# - Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
# - Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
# - Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
# - Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
# - Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
# Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, 
# the optimal closing time is 2.

customers_2 = "NNNNN"
# Output: 0
# Explanation: It is best to close the shop at the 0th hour as no customers arrive.

customers_3 = "YYYY"
# Output: 4
# Explanation: It is best to close the shop at the 4th hour 
# as customers arrive at each hour.

print(Solution().bestClosingTime(customers_1))
print(Solution().bestClosingTime(customers_2))
print(Solution().bestClosingTime(customers_3))
