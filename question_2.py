count_even = 0
count_odd = 0

for number in range (1, 100,):

	if number % 2 == 0:
		count_even += 1
		
	elif number % 2 != 0:
		count_odd += 1

print("Number of even:", count_even)
print("Number of odd:", count_odd)

 
