import random

MAX_BET_LINES=3
MIN_BET=1
MAX_BET=100
def deposit():
    while True:
        deposit_amount=input("Enter the amount you want to deposit :")
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if deposit_amount > 0:
                break;
            else:
                print("Enter amount greater than 0")
        else:
            print("Please enter a number")
    return deposit_amount

def get_number_of_lines():
    while True:
        lines=input("Enter the number of lines you want to bet :")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines < MAX_BET_LINES:
                break;
            else:
                print("Enter lines between 1 and "+str(MAX_BET_LINES))
        else:
            print("Please enter a number")
    return lines


def get_bet():
    while True:
        bet=input("Enter the $ amount you want to bet :")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET < bet < MAX_BET:
                break;
            else:
                print(f"Enter the bet amount  between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number")
    return bet



def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet=bet * lines
        if total_bet >  balance:
            print(f"You dont have enough to bet, your currect balace is : ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet amount is ${total_bet}")



symbol_count= {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

ROWS=3
COLS=3


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol ,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns =[]
    for _ in range(cols):
        column=[]
        current_columns=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_columns)
            current_columns.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(column)-1:
                print(column[row],end="|")
            else:
                print(column[row],end="")
        print()



columns=get_slot_machine_spin(ROWS,COLS,symbol_count)

