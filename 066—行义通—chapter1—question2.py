time_int = eval(input("请输入一个以秒记的时间（范围为1—86400）："))
hour_int = time_int//3600
minute_int = time_int%3600//60
second_int = time_int%60
print(hour_int,minute_int,second_int)

