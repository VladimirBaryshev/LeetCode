# https://leetcode.com/problems/gas-station
# June 30th interview #7



# Edge cases and constraints:
#   len(gas) >= 0
#   len(cost) = len(gas)
#   gas[i] >= 0
#   cost[i] >= 0
#   sum(gas) = sum(cost) ???

# Solution ideas:
#   worth case big0 = n**2
#   find max of gas and cost
#   gas - cost = balance #[-2, -2, -2, 3, 3]
#   find first positive balance item

def find_starting_gas_station(gas: list[int], cost: list[int]) -> int:
    
    if sum(gas)<sum(cost):
        return -1

    n = len(gas)
    diff = [i[0] - i[1] for i in zip(gas, cost)]

    total = 0
    res = 0

    for i in range(n):

        total += diff[i]

        if total < 0:
            res = i + 1
            total = 0

    return res




gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# Output: 3

gas_2 = [5,1,2,3,4]
cost_2 = [4,4,1,5,1]
# Output: 4


print(find_starting_gas_station(gas, cost))
print(find_starting_gas_station(gas_2, cost_2))


# Feedback:
#   обсудили edge cases и constraints (не забывай писать constraints) 
#   у задачи объемное условие, кажется, ты довольно быстро понял суть задачи, видно, что читал внимательно 
#   и понял на что обращать внимание в условии
#   В решении хорошо, что прошелся по worst case/baseline scenario и сказал, 
#   что сложность квадратичная



