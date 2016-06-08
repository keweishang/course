# Separate a string by sep from the rear 
name,space,price = raw_input().rpartition(' ')

# Iterate through dict items, each item is a tuple
for item_name, net_price in my_order.items():