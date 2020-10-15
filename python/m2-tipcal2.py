bill_amt = float(input("Enter total bill amount:\n"))
#service_lvl = input("Rate service good, fair, or bad\n")
tip_amount = 0
split = int(input("How many ways to split the bill?\n"))
print(split)
while tip_amount == 0:
    service_lvl = input("Rate service good, fair, or bad\n")
    if service_lvl == "good":
        tip_amount = float(bill_amt * .20)
    elif service_lvl == "fair":
        tip_amount = float(bill_amt * .15)
    elif service_lvl == "bad":
        tip_amount = float(bill_amt * .10)
    else:
        print("Only rate good,fair,or bad please!")
print(f"Your tip amount is {tip_amount}")
total = bill_amt  + tip_amount
print(f"Total Amount is {total}")
split_amt = total/split
print(f"Total amount per person is {split_amt}")