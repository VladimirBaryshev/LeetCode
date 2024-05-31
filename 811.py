# 811. Subdomain Visit Count
# https://leetcode.com/problems/subdomain-visit-count/description/


from typing import List
from collections import 


class Solution:

    def subdomainVisits(self, cpdomain: List[str]) -> List[str]:

        d = defaultdict(int) # subdomain_counts
        
        for cp in cpdomain:
            count, domain = cp.split(" ")
            count = int(count)
            domain = domain.split(".")

            for i in range(len(domain)-1,-1,-1): # ['google', 'mail', 'com']
                k = domain[i:]
                k = ".".join(k)
                d[k] += count

        return [str(v) + " " + k for k,v in d.items()] # {mail.com: 10, com: 2} => 10mail
    


cpdomains_1 = ["9001 discuss.leetcode.com"]
# Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
# Explanation: We only have one website domain: "discuss.leetcode.com".
# As discussed above, the subdomain "leetcode.com" and "com" will also be visited. 
# So they will all be visited 9001 times.


cpdomains_2 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# Explanation: We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
# For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

print(Solution().subdomainVisits(cpdomains_1))
print(Solution().subdomainVisits(cpdomains_2))



