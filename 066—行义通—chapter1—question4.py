#汽车的总数量
num_int = 5750000
#所有汽车的排放废气量(单位为克）
gas_int1 = num_int*15000*150
#单位为吨
gas_int2 = gas_int1/1000000
print("北京市2015年全年机动车排放废气为",gas_int2,"吨")
#北京市常住人口
population_int = 21140000
#平均每人吸入废气量
takein_float = gas_int1/population_int
print("平均每人吸入废弃量：",takein_float,"克")
