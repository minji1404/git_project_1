from dk_add import add
from dk_subtract import subtract
from dk_multiply import multiply
from dk_divide import divide

def calculator():
    a = float(input("1st number: "))
    b = float(input("2nd number: "))
    op = input("연산자 (+, -, *, /): ")
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    if op in operations:
        try:
            result = operations[op](a, b)
            print("result:", result)
        except Exception as e:
            print("오류:", e)
    else:
        print("Invalid operator.")

if __name__ == "__main__":
    calculator()
