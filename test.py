# t = [[1,3],[2,2],[3,1],[1,4]]

# t = sorted(t, key=lambda x: x[1])
# print(t)

# for i in range(len(t)-1, -1, -1):
#     print(t[i])


original = ["a","b","c","c","e","d","c","c","c"]
changed =  ["b","c","b","e","b","e","a","e","d"]
cost =     [ 2,  5,  5,  1,  2,  20, 100, 100, 100]

vertices = dict([(k,(v, c)) for k,v,c in zip(original, changed, cost)])
all_possible_routes = [{"path":[s,e], "cost":c} for s,e,c in zip(original, changed, cost)]

# print(vertices)
# print(all_possible_routes)
for d in all_possible_routes:
	if d["path"][-1] in vertices.keys():
		v = d["path"][-1]
		dest, cost = vertices[v]
		if dest not in d["path"]:
			d["path"].append(dest)
			d["cost"] += cost

for i in set(original):
	t = [d for d in all_possible_routes if d['path'][0]==i]
	t = sorted(t, key=lambda x:x['cost'])
	print(i,t, '\n')

