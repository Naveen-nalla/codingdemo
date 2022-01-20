n = int(input("Enter a number of items:"))

items = []
weights = {}
profits = {}

for i in range(n):
    print('')
    item = input("Enter item name:")
    items.append(item)
    weights[item] = int(input("Enter item weight:"))
    profits[item] = int(input("Enter item profit:"))
    
print()

sorted_weights = dict(sorted(weights.items(), key=lambda item: item[1], reverse=True))

sorted_items = list(sorted_weights.keys())

max_weight = int(input("Enter the max weight:"))

bag = {}

maximum_profit = 0

for i in range(n):
    j=i
    item = sorted_items[i]
    free_weight = max_weight
    result = {}
    temp_profit = 0
    
    while free_weight > 0 and j<n:
        selected_item = sorted_items[j]
        selected_weight = sorted_weights[selected_item]
        
        if(free_weight - selected_weight >= 0):
            if(result.get(selected_item) != None):
                result[selected_item] += 1
            else:
                result[selected_item] = 1
            free_weight -= selected_weight
            temp_profit += profits[selected_item]
        else:
            j += 1
            
    if maximum_profit < temp_profit:
        bag = result
        maximum_profit = temp_profit
        
print()

print("bag: ", bag)
print("profit: ", maximum_profit)
