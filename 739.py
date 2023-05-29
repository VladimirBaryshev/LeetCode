# 39. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

'''
    edge_cases:
    [100]
'''

'''
    Steps:
    0) use stack
        - compare with prev values retrospectivly
    1) create zeropadded vector
    2) iterrate input array by index and value
        - enumerate
'''

temperatures_1 = [73,74,75,71,69,72,76, 73 ] #[1,1,4,2,1,1,0,0]
temperatures_2 = [30,40,50,60] #[1,1,1,0]
temperatures_3 = [30,60,90] #[1,1,0]


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures) #[1,1,4,2,1,1,0,0]
    stack = []  # pair: [temp, index] #[(76, 6), (73, 7)]

    for i, t in enumerate(temperatures): # 7 73

        while stack and t > stack[-1][0]: # 73 > 76 False
            

            stackT, stackInd = stack.pop() # ...


            res[stackInd] = i - stackInd # ...


        stack.append((t, i)) # (73, 7)


    return res

dailyTemperatures(temperatures_1)


