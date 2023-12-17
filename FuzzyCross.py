def FuzzyCross(u_A_X ,u_B_X):
    return (u_A_X * u_B_X) / (u_A_X + u_B_X) 

set_1 = [0.1 , 0.2 , 0.3]
set_2 = [0.5 , 0.4 , 0.6]

for i in range(len(set_1)):
    print(FuzzyCross(set_1[i] , set_2[i]))