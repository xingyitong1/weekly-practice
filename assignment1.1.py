import random

while True:
    #S可代表的数为8或9
    S = random.randint(8,9)
    #E可代表的数为
    E = random.randint(0,9)
    #M可代表的数一定为1
    M = 1
    #O可代表的数为
    O = random.randint(0,9)
    #D可代表的数为
    D = random.randint(0,9)
    #R可代表的数为
    R = random.randint(0,9)
    #N可代表的数为
    N = random.randint(0,9)
    #Y可代表的数为
    Y = random.randint(0,9)
    money = M*10000+O*1000+N*100+E*10+Y
    send = S*1000+E*100+N*10+D
    more = M*1000+O*100+R*10+E
    if S!= E and S!=M and S!=O and S!= D and S!= R and S!=N and S!=Y:
        if E!=M and E!=O and E!= D and E!= R and E!=N and E!=Y:
            if M!=O and M!= D and M!= R and M!=N and M!=Y:
                if O!= D and O!= R and O!=N and O!=Y:
                    if  D!= R and D!=N and D!=Y:
                        if R!=N and R!=Y:
                            if N!= Y:
                                if send + more == money:
                                    print(send,more,money)
                                    break

        

