#author CJP 01/27/2022
groceries = [['apple','pear','banana',],['salmon','tuna','cod',],['milk','eggs','yogurt']]
costs = [1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]

def food_costs(groceries,costs):
    groceries_mod = groceries
    for row in groceries:
        thing = row[0]
        for x,y in enumerate(groceries,costs):
            thing = groceries[y] + ":" + str(costs[y])
    return groceries_mod

print(food_costs([['apple','pear','banana',],['salmon','tuna','cod',],['milk','eggs','yogurt']],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]) == 
['apple: $1.99','pear: $2.99','banana: $0.99',],['salmon: $9.99','tuna: $10.99','cod: $6.99',],['milk: $3.49','eggs: $2.49','yogurt: $1.49',])

