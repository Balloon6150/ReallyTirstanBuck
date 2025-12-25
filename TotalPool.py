treasury_pin = input("Enter the treasury pin to access Total Pool: ")
correct_treasury_pin = "1234"  # Example pin, replace with actual secure
money = open("TotalPoolMoney.txt", "r").read()
money = float(money)
if treasury_pin == correct_treasury_pin:
    type = input("Current action: Add, Remove, or View Total Pool Money? (a/r/v): ")
    if type.lower() == "a":
        add_amount = float(input("Enter amount to add to Total Pool: $"))
        money += add_amount
        print("Added $" + str(add_amount) + " to Total Pool.")
    print("Current Total. Pool Money is: $" + str(money))
    if type.lower() == "r":
        remove_amount = float(input("Enter amount to remove from Total Pool: $"))
        if remove_amount > money:
            print("Error: Cannot remove more than the current Total Pool amount.")
        else:
            money -= remove_amount
            print("Removed $" + str(remove_amount) + " from Total Pool.")
    open("TotalPoolMoney.txt", "w").write(str(money))
    if type.lower() == "v":
        print("Viewing Total Pool Money: $" + str(money))
print("Exiting Total Pool management.")