MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 10,
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
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

machine_water = resources["water"]
machine_milk = resources["milk"]
machine_coffee = resources["coffee"]

money = 0
condition = True
while condition:
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_coffee == "espresso" or user_coffee == "latte" or user_coffee == "cappuccino":
        ingredients = MENU[user_coffee]["ingredients"]
        new_water = machine_water - ingredients["water"]
        new_coffee = machine_coffee - ingredients["coffee"]
        new_milk = machine_milk - ingredients["milk"]
        #First: Checks If the resources are sufficient
        if new_water < 0:
            print("Sorry there is not enough water.")

        elif new_coffee < 0:
            print("Sorry there is not enough coffee.")

        elif new_milk < 0:
            print("Sorry there is not enough milk.")
        else:

            print("Please insert coins.")
            user_quarters = int(input("How many quarters?"))
            user_dimes = int(input("How many dimes?"))
            user_nickles = int(input("How many nickles?"))
            user_pennies = int(input("How many pennies?"))
            inserted_coins = (user_quarters * quarters) + (user_dimes * dimes) + (user_nickles * nickles) + (
                    user_pennies * pennies)

            #Secod: Checks the coins inserted
            if inserted_coins >= MENU[user_coffee]["cost"]:
                machine_water = new_water
                machine_coffee = new_coffee
                machine_milk = new_milk
                change = round(float(inserted_coins - MENU[user_coffee]["cost"]), 2)
                money += MENU[user_coffee]["cost"]
                print(f"Here is your {change}$ in change.Enjoy your {user_coffee} coffee!")

            else:
                print("Sorry that's not enough money. Money refunded.")


    elif user_coffee == "report":
        print(f"Water: {machine_water}ml\nMilk: {machine_milk}ml\nCoffee: {machine_coffee}g\nMoney: {money}$")

    elif user_coffee == "off":
        condition = False
        print("Bye")
    else:
        print("You typed wrong input,try again...")