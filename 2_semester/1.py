import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby

fig, ax = plt.subplots()
# data = np.random.rand(1000)
# print(data)

red = [
    7144.8,
    6973,
    6973,
    6973,	     
    6888.6,
    6888.6,
    6888.6,
    6703.8,
    6703.8,
    6703.8,
    6703.8,
    6676.6,
    6676.6,
    6676.6,
    6676.6,
    6601.9,
    6601.9,
    6601.9,
    6601.9,
    6539.2,
    6539.2,
    6539.2,
    6539.2,
    6513.5,
    6513.5,
    6513.5,
    6513.5,
    6417.6,
    6417.6,
    6417.6,
    6417.6,
    6392.9,
    6392.9,
    6392.9,
    6392.9,
    6349,
    6349,
    6349,
    6349,
    6320.1,
    6320.1,
    6320.1,
    6320.1,
    6291.5,
    6291.5,
    6291.5,
    6291.5,
    6225.9,
    6225.9,
    6225.9,
    6225.9
]

# red = [list(j) for i, j in groupby(red)]

orange = [
    6177.7,
    6177.7,
    6177.7,
    6177.7,
    6159.6,
    6159.6,
    6159.6,
    6159.6,
    6114.9,
    6114.9,
    6114.9,
    6114.9,
    6095,
    6095,
    6095,
    6095,
    6051.5,
    6051.5,
    6051.5,
    6051.5,
    5996,
    5996
]
# orange = [list(j) for i, j in groupby(orange)]

yellow = [
    5958.4,
    5958.4,
    5958.4,
    5958.4,
    5903.1,
    5903.1,
    5903.1,
    5903.1,
    5868.9,
    5868.9,
    5868.9,
    5868.9,
    5868.9,
    5868.9,
    5777.3,
    5777.3,
    5777.3,
    5666.1,
    5666.1,
    5666.1
]
# yellow = [list(j) for i, j in groupby(yellow)]

green = [
    5400.4,
    5400.4,
    5400.4,
    5400.4,
    5400.4,
    5339.8,
    5339.8,
    5328,
    5328
]
# green = [list(j) for i, j in groupby(green)]	

blue = [
    5105,
    5105,
    5065.6,
    5021.6,
    5021.6    
]
# blue = [list(j) for i, j in groupby(blue)]

plt.hist([red, orange, yellow, green, blue], color=[
         'red', 'orange', 'yellow', 'green', 'blue'], bins=70, width=36)
# plt.xlabel('Age')
# plt.ylabel('Person Count')
# plt.bar( width = 0.4)
plt.legend()
plt.show()

# data = red +orange + yellow + green + blue
# print(data)
# N, bins, patches = ax.hist(data, edgecolor='white', linewidth=1)
# print(patches)
# for i in range(0,len(red)):
#     patches[i].set_facecolor('red')

# for i in range(len(red),len(orange)):
#     patches[i].set_facecolor('orange')
# for i in range(len(orange),len(yellow)):
#     patches[i].set_facecolor('yellow')
# for i in range(len(yellow),len(green)):
#     patches[i].set_facecolor('green')
# for i in range(len(green),len(blue)):
#     patches[i].set_facecolor('blue')    
# plt.show()
