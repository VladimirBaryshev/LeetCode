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
    
    balance = [i[0] - i[1] for i in zip(gas, cost)]

    cur_balance = 0
    starting_point = 0

    for i in range(len(balance)):
        cur_balance += balance[i]
        if balance[i] > 0 and balance[starting_point] < balance[i]:
            starting_point = i      

    if cur_balance >= 0:
        return starting_point
    return -1

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



