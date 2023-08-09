import random

ROWS=3
COLUMNS=3

MAX_LINES=3
MAX_BET=100
MIN_BET=1

symbol_count={'A':1,'B':4,'C':6,'D':8}
symbol_value={'A':5,'B':4,'C':3,'D':2}


def check_winnings(columns,lines,bet,value):
    winnings=0
    winnings_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=value[symbol]*bet
            winnings_lines.append(line+1)
    return winnings,winnings_lines



def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for col in range(cols):
        column=[]
        current_symbols=all_symbols[:]

        for _ in range(rows):
            value=random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i !=len(columns) - 1:

                print(column[row],  end="|")
            else:
                print(column[row],end="")
        print()



def deposit():
    while True:
        amount=input("How much you goona deposit ? $ ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount should be greated than zero")
        else:
            print("number only")
    return amount


def get_number_of_lines():
    while True:
        lines=input("enter number of lines to bet on (1-"+str(MAX_LINES)+") ?  ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Enter valid number of lines ")
        else:
            print("number only")
    return lines


def get_bet():

    while True:
        bet_amt=input(" how much would you like to bet on each line ? $ ")
        if bet_amt.isdigit():
            bet_amt=int(bet_amt)
            if MIN_BET<=bet_amt<=MAX_BET:
                break
            else:
                print(f"Amount must be between $ {MIN_BET} - $ {MAX_BET}")
        else:
            print("number only")
    return bet_amt

def spin(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet * lines
        if total_bet>balance:
            print(f"You dont have enough money to bet $ {total_bet}, current balance is $ {balance}")
        else:
            break
    print(f"you are betting $ {bet} on {lines} lines. total betting ammount is $ {total_bet}")

    slots=get_slot_machine_spin(ROWS,COLUMNS,symbol_count)
    print_slot_machine(slots)
    winnings,winnings_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.  ")
    print(f"You won on lines ",*winnings_lines)
    return winnings-total_bet


def main():

    balance=deposit()
    while True:
        print(f"Current balance is $ {balance}")
        spinning=(input("Enter to spin (q to quit)"))
        if spinning=="q":
            break
        balance+=spin(balance)
    print(f"You left with $ {balance}.")
    
main()
