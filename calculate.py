a = input("계산하고 싶은 수 1 : ")
b = input("계산하고 싶은 수 2 : ")

a_int = int(a)
b_int = int(b)

cal = input("+, -, *, /, ^, % 중 자신이 하려고 하는 계산에 알맞은 기호를 선택하여 입력하시오 : ")

if cal == "+":
    print(a_int + b_int)
elif cal == "-":
    print(a_int - b_int)
elif cal == "*":
    print(a_int * b_int)
elif cal == "/":
    print(a_int / b_int)
elif cal == "^":
    print(a_int ** b_int)
elif cal == "%":
    print(a_int % b_int)
