def min_cost(cst, costs, A, best, i):
    temp = 0
    for j in costs[i+1]:
        if j[0] != i+1:
            temp = A[j[0]-1] + j[1]
            
            if temp < best:
                best = temp
            else:
                continue
            
            if j[0] in cst:
                best = min_cost(cst, costs, A, best, j[0]-1)
        
    return best


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        la = len(A)
        lb = len(B)
        best = 0
        best_cost = []
        temp = 0
        costs = {}
        for i in B:
            if i[0] not in costs:
                costs[i[0]] = [[i[1],2*i[2]]]
            else:
                costs[i[0]].append([i[1],2*i[2]])
            
            if i[1] not in costs:
                costs[i[1]] = [[i[0],2*i[2]]]
            else:
                costs[i[1]].append([i[0],2*i[2]])
        
        cst = list(costs.keys())
        #print(costs)
        for i in range(la):
            best = A[i]
            if i+1 in cst:
                best = min_cost(cst, costs, A, best, i)
            
            best_cost.append(best)
            
        return best_cost
