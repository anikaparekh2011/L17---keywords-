snack_price = 25

print("WELCOME TO THE SNACK VENDING MACHINE")
print(f"the snack price is {snack_price} units ")
print("WE ONLY EXCEPT 1, 5, 10, 25 COINS")

total_inserted = 0 
coins_inserted = 0 

while True: 
    coin = int(input("Please insert a coin: "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("this is not a suitable coin, insert a new one")
        continue
    total_inserted += coin 
    coins_inserted += 1

    if total_inserted >= snack_price:
        print("enough money given")
        break

def calc_change(paid, price):
    change =  paid - price 
    return change 

change_due =  calc_change(total_inserted, snack_price)
print(change_due)

if change_due == 0:
    pass
else: 
    print(f"here is your change {change_due}")