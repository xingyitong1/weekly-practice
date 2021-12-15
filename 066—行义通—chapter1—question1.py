#本金
money_int = 9
#整存整取
sum1_float = money_int*0.0305*5+money_int
#一年期
sum2_float = money_int*(1.0035)**5
print("整存整取五年的总额为：",sum1_float)
print("一年期五年的总额为：",sum2_float)
#存五年期多收入的钱
moremoney_float = sum1_float-sum2_float
print("存五年期多收入的钱：",moremoney_float)
