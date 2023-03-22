MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def generate_report():
        print(f"Water: {resources['water']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Milk: {resources['milk']}")
        print(f"Profit: ${profit}")

        
def check_resource(drink):
    for ingredient in resources.keys():
        if resources[ingredient] < MENU[drink].get("ingredients").get(ingredient):
            print(f'Sorry there is not enough ' + ingredient + ".")
            return False
        else:
            return True
        

def process_coins(drink, input_quarters, input_dimes, input_nickles, input_pennies):
    money_changer = {
        "quarters" : 0.25,
        "dimes" : 0.10,
        "nickles" : 0.25,
        "pennies" : 0.01
}
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0

    sum = float(input_quarters)*money_changer["quarters"] + float(input_dimes)*money_changer["dimes"] + float(input_nickles)*money_changer["nickles"] + float(input_pennies)*money_changer["nickles"]
    cost_of_drink = MENU[drink].get("cost")
    if cost_of_drink > sum:
        return False
    else:
        global profit
        profit += sum - cost_of_drink
        return profit
       

def make_coffee(drink):
    
    for key, value in resources.items():
        remaining_resource = resources[key] - MENU[drink].get("ingredients").get(key)
        resources[key] = remaining_resource
    
    return print(resources)

        
while True:
    choice = input( "What would you like? (espresso/latte/cappuccino):" ) 
    if choice == "off":
        print(f'Turning off the coffee machine...')
        exit 
    elif choice == "report":
        generate_report()
    else:
        check_resource(choice)
        if check_resource(choice) == False:
            break
        else:
            input_quarters = input("Please input the number of quarters")
            input_dimes = input("Please input the number of dimes")
            input_nickles = input("Please input the number of nickles")
            input_pennies = input("Please input the number of pennies")
            if process_coins(choice, input_quarters, input_dimes, input_nickles, input_pennies) == False:
                print(f'Sorry there\'s not enough money. Money refunded.')
                break
            else:
                profit = str(process_coins(choice, input_quarters, input_dimes, input_nickles, input_pennies)) 
                print(f'Here is $ ' + profit + " in change.")
                make_coffee(choice)




            





       
           
