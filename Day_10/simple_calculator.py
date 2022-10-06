from art import logo

#add
def add(n1,n2):
	return n1 + n2

#subtract
def subtract(n1,n2):
	return n1 - n2

#multiply
def multiply(n1,n2):
	return n1 * n2

#divide
def divide(n1,n2):
	return n1 / n2

#dictionary of operators: functions
operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide,
}

#run the calculator
def calculator():
  #executes only on initial run
	print(logo)
	num1 = float(input("What is the first number? "))
	#print out operator options
	for op in operations:
		print(op)
	
	calculate = True
	
	while calculate:
		operation_symbol = input("Choose an operator: ")
		
		num2 = float(input("What is the next number? "))
		
		answer = operations[operation_symbol](num1,num2)
		
		print(f"{num1} {operation_symbol} {num2} = {answer}")
		
    #either contiune with the output or start a new calculation
		if input(f"Do you want to continue with {answer} (y) or start new (n)? ") == "n":
			calculate = False
      #recursive call to restart function
			calculator()
		else:
      #set num1 to answer to continue calculation
			num1 = answer

calculator()
