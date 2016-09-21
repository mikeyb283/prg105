cost = 1
total_cost = 0
sales_tax = .06

print ("Input prices. Enter 0 to indicate that you are done entering.")

while cost != 0:
    strCost = raw_input("Item price: ")
    cost = float(strCost)
    total_cost += cost
else:
    print ("Item total is $" + str(total_cost))

tax = total_cost * sales_tax
grand_total = total_cost + tax
print ("Grand total: $") + str(round(grand_total, 2))
