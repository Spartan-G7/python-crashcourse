prompt = "\nPlease enter the topping you wish to add to your pizza!:"
prompt += "\n(Enter quit when finished)"

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(toppings.title(),"added!")
