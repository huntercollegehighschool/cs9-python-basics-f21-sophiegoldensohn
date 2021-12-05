'''
______
PART 3
______
There are (at least) 6 errors in this code. Fix them so that it runs properly.

'''

#original code starts here
#number1 = input("Enter a number: ")
#number2 = int(input("Enter another number: ")

#print "The sum of your numbers is", number1 + Number2
#print(Seven times your second number is, 7(number2))

number1 = int(input("Enter a number: "))
#error 1: missing parentheses, error 2: missing int
number2 = int(input("Enter another number: "))
#error 3: missing end parentheses
print ("The sum of your numbers is", number1 + number2)
#error 4: missing parentheses, error 5: capitalized N in number2
print("Seven times your second number is", 7 * number2)
#error 6: missing quotation marks, error 7: incorrect format for multiplication with 7(number2)