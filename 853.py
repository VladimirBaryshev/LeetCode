# 853. Car Fleet
# https://leetcode.com/problems/car-fleet/

# Output = 3
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
target = 12


def mapper(position, speed, target):

    pair = list(zip(position, speed))
    pair.sort(reverse=True) # Reverse Sorted Order


    # [(10,2), (8,4), (5,1), (3,3), (0,1)]
    # [(8,4), (5,1), (3,3), (0,1)]
    # [(5,1), (3,3), (0,1)]
    # [(3,3), (0,1)]
    # [(0,1)]

    stack = [] # [1,7,12]

    for p, s in pair:  #  (0,1)

        stack.append((target - p) / s) # (12 - 0) / 1

        if len(stack) >= 2 and stack[-1] <= stack[-2]: # False
            stack.pop() # ...

    return len(stack)

print(mapper(position, speed, target))    