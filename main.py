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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
PENNY = 0.01
DIME = 0.10
NICKEL = 0.05
QUATER = 0.25
is_on = True
not_enough = 0


while is_on == True :
    # TODO-1 : Prompt user by asking What would you like?
    choice = input("what would you like ? (espresso/latte/cappuccino) : ")
    # TODO-2 :Turn off the Coffee Machine by entering to the prompt.
    if choice == 'off':
        is_on = False
    # TODO-3:Print report.
    elif choice == 'report':
        print(f"water:{resources['water']}ml")
        print(f"milk: {resources['milk']}ml ")
        print(f"coffee: {resources['coffee']}g")
        print(f"money:${profit}")
    #TODO-4:Check resources sufficient?
    else:
        list = MENU[choice]
        ingred = list['ingredients']
        for i in ingred:
            if ingred[i] > resources[i]:
                not_enough += 1
        if not_enough > 0:
            print("Sorry,not enough resources \n")
        # TODO-5:Process coins.
        if not_enough == 0:
            print("please insert coins")
            quaters_amt = int(input("How many quarters:"))
            nickle_amt = int(input("How many nickel:"))
            dime_amt = int(input("How many dime: "))
            penny_amt = int(input("How many penny :"))
            amount = (quaters_amt * QUATER) + (nickle_amt * NICKEL) + (dime_amt * DIME) + (penny_amt * PENNY)
            # TODO-6:Check transaction successful?
            if amount < list['cost']:
                print("Sorry that's not enough money. Money refunded.")
            elif amount >= list['cost']:
                    for i in ingred:
                        resources[i] -= ingred[i]
                    change = amount - list['cost']
                    profit += list['cost']
                    print(f"Here is ${round(change,2)} in change.")
                    print(f"Here is your {choice} ☕️. Enjoy! ")


