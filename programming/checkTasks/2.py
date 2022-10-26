from concurrent.futures import process
import random

product = ['Яблоки', 'Хлеб', 'Молоко', 'Гвозди', 'Ряженка', 'Чурчхелла']
cost = []
for i in product:
    cost.append(random.randint(10, 150))
price = []
for i in cost:
    price.append(i*1.15)
    
array = list(zip(product, cost, price))
print(array)