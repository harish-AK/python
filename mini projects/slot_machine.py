MAX_LINES=5
MAX_BET=100
MIN_BET=1
def deposit():
    while True:
        amount=input("How much you goona deposit ?   ")
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
        lines=input("enter number of lines to bet on (1-"+str(MAX_LINES)+") ?    ")
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
        bet_amt=input(" how much would you like to bet on each line ?  ")
        if bet_amt.isdigit():
            bet_amt=int(bet_amt)
            if MIN_BET<=bet_amt<=MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("number only")
    return bet_amt

def main():

    balance=deposit()
    lines=get_number_of_lines()
    bet=get_bet()
    total_bet=bet * lines
    print(f"you are betting $ {bet} on {lines} lines. total betting ammount is $ {total_bet}")
main()