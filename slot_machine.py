# Author: Kade Carlson
# Date: 12/30/2022
# Slot Machine program that is going to be used to test my skills. Slot machine of 3 lines, players can bet on a chosen number of
# lines from 1 to 3. If a row has all the same symbols then it's a win and their bet is multiplied by that symbol's value.

# Imports
import os
import random

# Constants
MAX_BET = 1000
MIN_BET = 10
SYMBOLS = ["@", "#", "%", "&"]
SYMBOL_VALUES = {"@": 2, "#": 3, "%": 5, "&": 7}


def set_balance():
    """Ask the user for the amount of money that they would like to deposit into their account."""
    balance = int(input("How much would you like to deposit?: $"))
    if balance <= 0:
        os.system("cls")
        print("Please input an amount greater than $0...")
        balance = set_balance()

    return balance


def set_bet(balance):
    """Ask the user for the amount of money that they would like to bet and on how many lines."""
    bet = int(input("How much would you like to bet?: $"))
    if not MIN_BET <= bet <= MAX_BET:
        os.system("cls")
        print(f"Please bet an amount between ${MIN_BET} and ${MAX_BET}")
        bet = set_bet(balance)

    if bet > balance:
        os.system("cls")
        print(f"Not enough money. Your balance is ${balance}.")
        bet = set_bet(balance)

    return bet


def set_lines(balance, bet):
    """Ask the user for how many lines they want to bet on."""
    lines = int(input("How many lines do you want to bet on (1-3)?: "))
    if not 1 <= lines <= 3:
        os.system("cls")
        print("You must bet on either 1, 2, or 3 lines")
        lines = set_lines(balance, bet)

    if bet * lines > balance:
        os.system("cls")
        print(f"Not enough money. Your balance is ${balance}. Your bet is ${bet}.")
        lines = set_lines(balance, bet)

    return lines


# Print the slot machine
def print_machine():
    """Prints the slot machine with the symbols in a 3x3 format."""
    row = []
    copy_row = []
    for i in range(9):
        row.append(random.choice(SYMBOLS))
        if (i + 1) % 3 == 0:
            print("", end="|")
            for symbol in row:
                print(symbol, end="|")
            print()
            print("-------")
            copy_row.append(row)
            row = []

    return copy_row


def get_symbol_value(symbol):
    """Returns the symbol value that the bet is multiplied by."""
    for key, value in SYMBOL_VALUES.items():
        if key == symbol:
            return value


# Check for wins, add winnings to deposit balance
def check_winnings(rows, bet, balance):
    for row in rows:
        for symbol in row:
            if symbol != row[0]:
                balance -= bet
                break
        else:
            balance += bet * get_symbol_value(symbol)

    return balance


def game(balance):
    """This function contains the game logic"""

    bet = set_bet(balance)
    lines = set_lines(balance, bet)
    print(f"Your balance is ${balance}")
    print(f"You bet ${bet}")
    print(f"You bet on {lines} lines for a total bet of ${bet * lines}")
    rows = print_machine()
    new_balance = check_winnings(rows[0:lines], bet, balance)
    print(f"Your new balance is: ${new_balance}")

    return new_balance


def main():
    balance = set_balance()
    new_balance = game(balance)

    query = input(
        "Press q to quit, d to deposit more, or any other key to make another bet: "
    )
    while query != "q":
        if new_balance < MIN_BET:
            query = input(
                f"Balance below minimum bet (${MIN_BET}). Press q to quit or d to deposit more: "
            )
            if query != "q" or query != "d":
                print("Can't bet more. Bye")
                break
        if query == "d":
            new_balance += set_balance()
            print(f"Your new balance is ${new_balance}")
            game(new_balance)
        else:
            game(new_balance)
        query = input(
            "Press q to quit, d to deposit more, or any other key to make another bet: "
        )


if __name__ == "__main__":
    main()
