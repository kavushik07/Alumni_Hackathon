import json
import lvl0 
i='Input data\level1a.json'

with open(i,'r') as inp:
    data=json.load(inp)

def knapsack(wt, val, W, n): 
    if n == 0 or W == 0: 
        return 0
    if t[n][W] != -1: 
        return t[n][W] 
    
    if wt[n-1] <= W: 
        t[n][W] = max( 
            val[n-1] + knapsack( 
                wt, val, W-wt[n-1], n-1), 
            knapsack(wt, val, W, n-1)) 
        return t[n][W] 
    elif wt[n-1] > W: 
        t[n][W] = knapsack(wt, val, W, n-1) 
        return t[n][W] 

dicton = {}
dicton['W'] = data['vehicles']['v0']['capacity']
profit={}
weight = {}
for i in data['neighbourhoods'].keys():
    profit[i] = data['neighbourhoods'][i]['order_quantity']
profit_list=list(profit.values())
for i in data['neighbourhoods'].keys():
    weight[i] = data['neighbourhoods'][i]['distances']
w_list=list(weight.values())

W = 600
n = len(profit) 
t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
#print(knapsack(W, w_list, profit_list, n)) 

inp.close()