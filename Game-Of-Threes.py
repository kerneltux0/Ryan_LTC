#set variables
print("Please enter a number")
rawInp = input()
number = int(rawInp)
#start while loop
while number != 1.0:
#check if divisible by 3
	if number % 3==0:
#if divisible, divide by 3 & repeat
		number = number / 3
		print(number)
	if number % 3==2:
#if not divisible, add or subtract 1 then divide by 3 & repeat
		number = number + 1
		print(number)
		number = number / 3
		print(number)
#print each stage
if number % 3==1:
#if not divisible, add or subtract 1 then divide by 3 & repeat
		number = number - 1
		print(number)
		number = number / 3
		print(number)
if number % 3==3:
#if not divisible, add or subtract 1 then divide by 3 & repeat
		number = number + 1
		print(number)
		number = number / 3
		print(number)
if number % 3==4:
#if not divisible, add or subtract 1 then divide by 3 & repeat
		number = number - 1
		print(number)
		number = number / 3
		print(number)
if number % 3==5:
#if not divisible, add or subtract 1 then divide by 3 & repeat
		number = number - 1
		print(number)
		number = number / 3
		print(number)
