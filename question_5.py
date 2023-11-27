total = 0
counter = 0
integer_number = int(input("Enter an Integer"))
while integer_number != 0:
	total = total + integer_number
	counter += 1
	integer_number = int(input("enter 0 to Quit"))
	Average = total/counter