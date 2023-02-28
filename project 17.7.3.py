per_cent = {'TCB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}

money = int(input("Enter the amount of money to be deposited: "))
deposit = [int(money * per_cent[bank] / 100) for bank in per_cent]

print("Deposit amounts:", deposit)

max_deposit = max(deposit)
print("Maximum amount you can earn:", max_deposit)