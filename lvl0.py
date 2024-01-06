import json

i='Input data\level0.json'

with open(i,'r') as f:
    data = json.load(f)

dicton = {}
dicton['r0'] = data['restaurants']['r0']['neighbourhood_distance']
for i in data['neighbourhoods'].keys():
    dicton[i] = data['neighbourhoods'][i]['distances']
count = 1
for i in dicton.keys():
    if i!='r0':
      dicton[i].insert(0,dicton['r0'][count])
      count+= 1
    else:
      dicton['r0'].insert(0,0)
print(dicton)

def TSP(c):
    global cost 
    adj_vertex = -1
    visited[c] = 1
    path.append(keys[c])
    min_val = 9999999
    for k in range(n):
        if (tsp_g[c][k] != 0) and (visited[k] == 0):
            if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if (min_val != 9999999):
      cost = cost + min_val
    if adj_vertex == -1:
        adj_vertex = 0
        path.append(keys[adj_vertex])
        cost = cost + tsp_g[c][adj_vertex]
        return
    TSP(adj_vertex)

path = []
keys = [i for i in dicton.keys()]

n = 21
cost = 0
visited = [0]*n
tsp_g = [i for i in dicton.values()]

TSP(0)

o='level0_output.json'
output = {}
output['v0'] = {}
output['v0']['path'] = path
with open(o,'w') as out:
    json.dump(output,out)
out.close()