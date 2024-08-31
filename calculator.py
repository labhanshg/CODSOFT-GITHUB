#Getting user input
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")             
num2 = float(input("Enter the second number: "))

#Calculate the result

result = 0
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1/num2

else:
    print("Invalid operator! Please enter +, -, *, /")
    result()

#Display the result
print("Result: ", result)