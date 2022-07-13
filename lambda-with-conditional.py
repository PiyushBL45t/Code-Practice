help('lambda')

add = lambda a, b: a + b
print(add(5, 5))
 
# output: 10

subtract = lambda a, b: a - b
print(add(100, 50))
 
# output: 50

multiply = lambda a, b: a * b
print(multiply(100, 50))
 
# output: 5000

variable_name = lambda parameters : code_for_if if (condition) else code_for_else

conditional_lambda = lambda x: x/100 if x < 20 else x
print(conditional_lambda(4))
 
# output: 0.04

# setup lambda 
check = lambda num : print(num, 'is Even') if num%2 == 0 else print(num, ' is Odd')
 
# input from user
num = int(input('Enter any number: '))
a = check(num)
print(a)

check = lambda a, b : print(a,'is divisible by', b) if (a%b == 0) else print(a ,' is indivisible by ', b)
a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))
obj = check(a, b)

