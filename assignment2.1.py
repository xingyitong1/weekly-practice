
try:
    A = int(input("enter the first number"))
    B = int(input("enter the second number"))
    C = int(input("enter the third number"))
    result = A/B
    C+= result
except ValueError:
    print("出现了ValueEorror错误")
except ZeroDivisionError:
    print("出现了ZeroDivisionError错误")
else:
    print("没有出现错误")
finally:
    print("无论是否出现错误都会执行的语句")
