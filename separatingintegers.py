fivedigitsinputs = int(input("Enter five digits"))

first_digit = fivedigitsinputs % 10;
firstRemainder = fivedigitsinputs // 10;
seconddigitsinput = firstRemainder % 10;
secondRemainder = firstRemainder // 10;

thirddigitsinputs = secondRemainder % 10;
thirdRemainder = secondRemainder // 10;
fourthdigitsinput = thirdRemainder % 10;
fourthRemainder = thirdRemainder // 10;

print(fourthRemainder,fourthdigitsinput ,thirddigitsinputs , seconddigitsinput, first_digit);