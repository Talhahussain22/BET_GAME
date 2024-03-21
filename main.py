import random
Max_lines=3
Rows=3
Col=3

def deposit():
    while True:
        amount=input("How much would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than zero")

        else:
            print("Enter a number")
    return amount

def Lines():
    while True:
        line=int(input(f"To how many lines you want to bet (1-{Max_lines}):"))
        if 1<=line<=3:
            break
        else:
            print("Enter value between (1-3)")

    return line
def bet():
    while True:
        income=int(input('What would you like to bet on each line? $'))
        if 0<income<=100:
            break
        else:
            print("Enter amount between (1-100)$")
    return income
def generator():
    l = ['A', 'B', 'C', 'D']
    generate = [[random.choice(l) for _ in range(Col)] for _ in range(Rows)]
    return generate
def winning(lines,bet,gen):
    win=0
    total_bet=bet*lines
    for i in range(lines):
        symbol=gen[i][i]
        for j in range(Rows):
            if symbol!=gen[i][j]:
                break
        else:
            win+=4*bet
    amount_winning=win-total_bet
    return win,amount_winning




def print_slot_machine(gen):
    for row in gen:
        for col in row:
            print(col,end=" | ")
        print()
def spin(amount):
    lines = Lines()
    while True:
        income=bet()
        total_bet=income*lines
        if total_bet>amount:
            print("You don't have enough balance for this spin!")

        else:
            print(f"You are betting {income}$ on {lines} lines . Total bet is {total_bet}$")
            gen=generator()
            print_slot_machine(gen)
            won=winning(lines,income,gen)
            amount+=won[1]
            print(f"You have won {won[0]}$")
            break
    return amount

def main():
    amount=deposit()
    while amount>=1:
        print(f"Your current balance is {amount}$")
        ask=input("Press Enter to continue and (q for quit)!").lower()
        if ask=="q":
            break
        else:
            amount=spin(amount)


main()