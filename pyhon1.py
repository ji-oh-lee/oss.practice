### 사칙연산
def add(num1,num2):
    return num1+num2

num1 = int(input("num1:"))
num2 = int(input("num2:"))
op = input("op:")

if op == '+': print(num1+num2)
elif op == '-': print(num1-num2)
elif op == '*': print(num1*num2)
elif op == '/': print(num1/num2)
