t = [[1,3],[2,2],[3,1],[1,4]]

t = sorted(t, key=lambda x: x[1])
print(t)

for i in range(len(t)-1, -1, -1):
    print(t[i])