def fractional_knapsack():
    weights=[20,30,10]
    values=[100,120,60]
    capacity=50
    res=0
    items = sorted(zip(weights,values),key = lambda x: x[1]/x[0],reverse = True)
    print(items)
    for pair in items:
        if capacity == 0:
            break
        elif (capacity - pair[0] >= 0):
            res += pair[1]
            capacity -= pair[0]
        else:
            res += capacity * pair[1]/pair[0]
            capacity = 0     

    print(res)
       
    
if __name__=="__main__":
    fractional_knapsack()
