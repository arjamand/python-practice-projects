# Coffee Machine Project

## Description

This project is a simple coffee machine program that allows the user to order various coffee drinks (espresso, latte, cappuccino) and interact with the coffee maker to process the orders.

The coffee machine is built using Python and consists of three main classes:

- `Menu`: Holds the list of available drinks.
- `CoffeeMaker`: Handles the resources and coffee making process.
- `MoneyMachine`: Deals with the payment processing.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/arjamand/python-practice-projects.git
```

2. Navigate to the project directory:
```bash
cd CoffeeMachineApp
```
## Usage
Run the coffee_machine.py script:
```bash
python main.py
```
Follow the on-screen instructions to choose a coffee drink and process your order.

## How It Works

The user is presented with a menu of available coffee drinks (espresso, latte, cappuccino).
The user enters their choice, and the program checks if the selection is valid.
If the selection is valid, the program checks if there are enough resources (water, milk, coffee) to make the drink.
If there are sufficient resources, the program prompts the user to insert coins for payment.
The user enters the payment amount, and the program verifies if the payment is successful.
If the payment is successful, the coffee maker processes the order, and the user is served their chosen drink.
If there are insufficient resources or the payment fails, the user is informed accordingly.
## Contributing
Contributions to this project are welcome! If you find any issues or want to add new features, feel free to open a pull request. Please make sure to follow the project's code style and guidelines.

## License
This project is licensed under the MIT License.


