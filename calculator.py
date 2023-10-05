def calci(a,b):
    operator = input("Mention a operator - '+','-','*','/','%': ")
    if operator == '+':
        return a+b
    elif operator =='-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator =='/':
        return a/b
    elif operator == '%':
        return a%b

a = int(input("Enter the first number: "))
b = int(input("ENter the second number: "))

res = float(calci(a,b))

print(f"The answer is {res}")