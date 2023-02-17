import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file = open('lab1.txt').readlines()
data = []
for i in file: 
    data.append(float(i[0:-1]))

data_minimum = min(data) 
data_maximum = max(data) 
average_value = sum(data)/len(data)

N = len(data)
square_deviation = []
deviation = []

for i in range(0, N):
    deviation.append((data[i] - average_value))

for i in range(0, N):
    square_deviation.append(deviation[i]**2)

average_square_deviation = (sum(square_deviation)/(N-1))**(1/2)
confidence_interval = (2.0086*average_square_deviation)/(N)**(1/2) 
relative_error = (confidence_interval/average_value)*100

c1 = 0
c2 = 0
c3 = 0
for i in data:
    if average_value - average_square_deviation < i < average_value + average_square_deviation: 
        c1+=1
    if average_value - 2*average_square_deviation < i < average_value + 2*average_square_deviation: 
        c2+=1
    if average_value - 3*average_square_deviation < i < average_value + 3*average_square_deviation: 
        c3+=1        

probability1 = c1/N 
probability2 = c2/N 
probability3 = c3/N

print('Минимум', data_minimum)
print('Максимум', data_maximum)
print('Среднеарифметическое значение', average_value)
print('Среднеквадратичное отклонение', average_square_deviation)
print('Доверительный интервал', confidence_interval)
print('Относительная погрешность', relative_error)
print('Вероятности:', probability1, probability2, probability3)


sns.displot(data, bins = 10, kde=True)
plt.show()