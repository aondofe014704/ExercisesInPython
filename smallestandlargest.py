number1 = int(input("Enter Three Integers  "))

number2 = int(input("Enter Three Integers  "))

number3 = int(input("Enter Three Integers  "))

sum = number1 + number2 + number3

print(sum)

average = number1 + number2 + number3 / 3
print(average)

product = number1 * number2 * number3
print(product)

largest = 0
smallest = number1

if number1 > largest:
       largest=number1

if number2 > largest:
     largest = number2

if number3 > largest:
    largest = number3
print(largest,'is the highest number')

if number1 < smallest:
	lowest = number1
if number2 < smallest:
	lowest = number2
if number3 < smallest:
	lowest = number3
print(smallest,'is the lowest number')
