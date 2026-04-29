### 사칙연산
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

num1 = int(input("num1:"))
num2 = int(input("num2:"))
op = input("op:")

if op == '+': print(add(num1+num2))
elif op == '-': print(sub(num1-num2))
elif op == '*': print(mul(num1*num2))
elif op == '/': print(div(num1/num2))