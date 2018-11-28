""" Purpose is to divide a receipt evenly
"""


""" Inputs:
		subtotal - float : price of receipt before tax/tip
		total - float: total after tax (no tip)
		tip_percent - float: percent to tip in decimal form ie. .20 -> 20 percent tip
		items - list of floats: prices of item a person ordered
	Outputs:
		float: price person owes 
"""
def get_amount_due(subtotal, total, tip_percent, items):
	tax_percent = ((total-subtotal)/subtotal)*100
	amount_due = 0
	for item in items:
		tax = item*(tax_percent)
		tip = item*(tip_percent)
		item_total = item + tax + tip
		amount_due += item_total
	return amount_due


def __main__():
	subtotal = input("What is the subtotal on you're receipt? (before tax and tip): ")
	total = input("What is the total of you're reciept? (After tax, no tip): ")
	tip_percent = input("What pecent would you like to tip, in decimal form? (ie. .20 -> 20 percent tip): ")
	items = []
	while True:
		item = input("Either enter the price of an item, or right 'done' in all lowercase: ")
		if item == 'done':
			break
		items.append(item)

	print ("The total amount due is : $" + str(get_amount_due(subtotal, total, tip_percent, items)))



