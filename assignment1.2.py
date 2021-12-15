flag = False#打一个标签方便退出循环
while not flag:
    A = eval(input("enter the first integer"))
    B = eval(input("enter the second integer"))
    cont = 0
    while B!=0:
        if B%2 == 1:
            cont+= A
        B = B//2
        A= A*2
    print(cont)
    Y_or_N = input("find another product?Yes or No?")
    while Y_or_N!= "Yes" and Y_or_N!= "No":#用户输的不对就一直让他输入
        Y_or_N = input("please enter Yes or No!")
    if Y_or_N == "No":
        flag = True#如果为No，改变标签推出循环
        print("Thank you!Goodbye!")
