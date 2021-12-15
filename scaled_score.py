scaled_title=['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','89-90','90-99','100']
scaled_score=[0,0,0,0,0,0,0,0,0,0,0]

while True:
   number=input("输入分数，一次输入一个分数，结束时请以'#'号结束：")
   if number=="#":
       break
   number=int(number)
   scaled_score[number//10]=scaled_score[number//10]+1

for i in range(len(scaled_score)):
   print('{:5s}的人数为{}'.format(scaled_title[i], scaled_score[i]))
