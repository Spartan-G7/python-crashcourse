sandwich_orders = ['pastrami','cuban','pastrami','italian','pastrami']
finished_sandwiches = []

for sandwich in sandwich_orders[:]: 
    if sandwich == 'pastrami':
        print("Sorry, we're out of pastrami.")
        sandwich_orders.remove('pastrami')  
    else:
        print(sandwich, "sandwich is complete.")
        finished_sandwiches.append(sandwich)
print(finished_sandwiches, "sandwiches are complete.")