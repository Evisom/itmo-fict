t_1 = float(input('T_1:'))
v_1 = float(input('V_1:'))
t_2 = float(input('T_2:'))
v_2 = float(input('v_2:'))

def getDistance(t1,v1,t2,v2):
    # Возвращаем сумму произведений
    return round(t1*v1+v2*t2, 2)

print(getDistance(t_1, v_1, t_2, v_2))