# To generate the slot machine values randomly we "import random".
import random

# Capital letters are a convention for constant values.
MAX_LINES = 3
MIN_LINES = 1
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3


# Setting up a dictionary for all the symbols in the reel of the slot.
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Value of each symbol.
symbol_value = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1
}


# To generate the outcome of the slot machine visible to user, using the above dict. and "ROWS" and "COLS".
# rows cols and symbols are the parameters which are going to be used in this function.
def output_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # When you use ".items "it gives you the key and the value associated with it, in the dictionary.
    # eg: symbol is going to be A and symbol_count is going to be 2

    for symbol, symbol_count in symbols.items():
        # '_' is an anonymous variable which is used when we don't care about count and only want to loop through.
        # Since symbol_count is 2 in the example, it will append 'A' twice to the all symbols list.
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # columns will be a nested list.
    columns = []
    for _ in range(cols):
        # column will be the lists inside the nested list columns.
        column = []

        # We create another list which is a copy of the all_symbols list and use the copy to take elements from.
        # That way, for every column the list will get updated to the default list.
        # To copy a list, '[:]' is used. This way, changes made to one list won't affect the other.
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            # Removing the random value generated from the list.
            current_symbols.remove(value)
            # Appending the 'value' to the column list.
            column.append(value)
        # Appending column to the columns list.
        columns.append(column)

        return columns


# functions like "def" execute a certain block of code and can return us the value whenever we ask for it.
def deposit():
    # while loop is used cuz we're gonna continuously ask the user to enter an amount until its valid.
    # "while True" is used to run the loop without any certain condition.
    while True:
        amount = input("What would you like to deposit? $")
        # Checking if the amount is a digit(str) not something like "hello world".
        if amount.isdigit():
            # Converting string input into integer input if it's a digit.
            amount = int(amount)
            if amount > 0:
                # Breaks out of the while loop as all conditions are met.
                break
            else:
                print("Please enter a valid amount.")
        # If amount is not digit:
        else:
            print("Please enter a valid input.")

    # To call this function we just write its name. eg: amount()
    return amount


# To determine how much they want to bet and how many lines they want to bet on.
# Multiply the bet amount by the no. of lines.
def input_of_no_of_lines():
    while True:
        lines = input(f"Enter the number of lines {MIN_LINES}-{MAX_LINES}: ")
        # Checking if lines is a digit(str) not something like "hello world".
        if lines.isdigit():
            # Converting string input into integer input if it's a digit.
            lines = int(lines)
            if 1 <= lines <= 3:
                # Breaks out of the while loop as all conditions are met.
                break
            else:
                print("Please enter valid number of lines.")
        # If lines is not digit:
        else:
            print("Please enter a valid input.")

    # To call this function we just write its name. eg: lines()
    return lines


def input_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        # Checking if the amount is a digit(str) not something like "hello world".
        if amount.isdigit():
            # Converting string input into integer input if it's a digit.
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                # Breaks out of the while loop as all conditions are met.
                break
            elif amount<=0:
                print("amount must be greater than 0.")
            else:
                print(f"amount must be between ${MIN_BET} and ${MAX_BET}.")
        # If amount is not digit:
        else:
            print("Please enter a valid input.")

    # To call this function we just write its name. eg: amount()
    return amount


# Converting rows into columns.
def slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    # If they bet on 1 line, then loop will run till line's index is 0, not including 1 therefore only once.
    for line in range(lines):
        # We need to take every element of the first column as a reference to check if the row has matching elements.
        # element inside 'column' list which is the first element of every row, which is inside a 'çolumns' list.
        symbol = columns[0][line]
        # loops through every column/element in columns.
        for column in columns:
            # 'line' will remain constant for every iteration.
            # But we will go through every 'column' list and check the see if corresponding elements are matching.
            # eg: line=0. Column will take every value and symbols being checked will be each column's element at line=0
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        # This else statement will tell us that we didn't break out of the for loop.
        # We can use for-else.
        # If it breaks, this else won't run. But if it doesn't, then the else statement will run after every iteration.
        else:
            winnings += values[symbol] * bet
            # We do +1 as line variable is an index.
            winning_lines.append(line + 1)

    return winnings, winning_lines


def spin(balance):
    lines = input_of_no_of_lines()
    while True:
        bet = input_bet()
        total_bet = bet * lines
        left = total_bet - balance

        if total_bet > balance:
            print(f"You need to deposit ${left} more to play.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")

    slots = output_slot_machine_spin(ROWS, COLS, symbol_count)
    slot_machine(slots)
    # We pass slots through check_winnings as slots, returns us the columns.
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    # the "*" splat operator will pass every single line from the "winning_lines" list to the print function below.
    print(f"You won {winnings}, at", *winning_lines)

    return winnings - total_bet


def main():
    # Main function is used for rerunning the program once it is over.
    # eg: so say, if they want to play again...it will rerun this main function.
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press enter to play.(q to quit): ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"you left with ${balance}")

