COFFEE MACHINE PROJECT (PROCEDURAL PROGRAMMING SOLLUTION)
A Python-based coffee machine program that simulates the functionality of a real coffee vending machine. The program allows users to select from three types of coffee (espresso, latte, cappuccino), and checks if there are sufficient resources before proceeding. It also handles coin inputs, checks if the inserted money is sufficient, and calculates any necessary change.

Features

a. Coffee Options: Choose between espresso, latte, and cappuccino.
b. Resource Management: Automatically checks the availability of ingredients (water, milk, and coffee) for each order.
c. Coin Handling: Accepts quarters, dimes, nickels, and pennies as input, ensuring the user pays enough for their coffee.
d. Change Calculation: Calculates and returns change when more money is inserted than required.
e. Inventory Report: A report command shows the current status of the machine's resources and money.
f. Shutdown: Use the off command to turn off the machine.

How It Works:

1. Choose a Coffee: The program prompts the user to choose a type of coffee.
2. Resource Check: It checks if enough ingredients are available for the chosen coffee.
3. Insert Coins: If ingredients are sufficient, the program asks for coin input.
4. Sufficient Payment: If the inserted amount covers the coffee's cost, it dispenses the drink and updates the resource inventory. If not, it refunds the money.
5. View Report: The report command displays the remaining ingredients and total money collected.
