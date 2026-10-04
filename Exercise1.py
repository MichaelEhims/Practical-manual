print('Amigos! I am practising python programming.')

num1 = int(input("kindly input a number:\n"))
operator = input('now select your preffered operator: +,–,÷,×,/ %')
num2 = int(input('another number'))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1- num2

else :
    print('invalid')
    

