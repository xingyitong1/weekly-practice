a=eval(input("输入第一个数:"))
b=eval(input("输入第二个数;"))
if a<b:
    a,b=b,a
r=b%a
while r!=0:
    a=b
    b=r
    r=b%a
print(b)
