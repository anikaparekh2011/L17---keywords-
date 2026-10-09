ticket_price = 25

print("PARKING TICKET")
print(f"YOU HAVE STAYED FOR 2 HOURS you must pay {ticket_price} coins")
print("WE ONLY EXCEPT 1, 5, 10, 25 COINS")

total_inserted = 0 
coins_inserted = 0

while True: 
    coin = int(input("PLEASE INSERT A COIN"))
    if coin != 1 or != 5 or !=10 or != 25:
        print("this aint a suitable coin, insert a new one")
        continue
    total_inserted = total_inserted + coin 
    coins_inserted = coins_inserted + 1

    if total_inserted >= ticket_price:
        print("enough money is given ")
        break

    def calc_change(paid, price):
        change = paid - price
        return change 

    change_due =  calc_change(total_inserted, ticket_price)
print(change_due)

if change_due == 0:
    pass
else:
    print(f"here is your change {change_due} coins")