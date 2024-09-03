# 929. Unique Email Addresses

from typing import List

class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        
        d = set()
        for e in emails:

            e = e.split("@")

            local_name = ""
            for i in e[0]:

                if i == ".":
                    continue

                if i == "+":
                    break

                local_name += i

            mail = local_name + "@" + e[1]
            d.add(mail)

        return len(d)


emails_1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

emails_2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3

print(Solution().numUniqueEmails(emails_1))
print(Solution().numUniqueEmails(emails_2))
