class Coffee:
    def __init__ (self, additive=None):
        self.additive = additive 
    def show_my_drink(self):
        if self.additive == None or self.additive == '':
            print('Черный кофе')
        else:
            print('Кофе и ' + self.additive)

latte = Coffee('молоко')
americano = Coffee()
americano.show_my_drink()
latte.show_my_drink()

userCoffee = Coffee(input('Введите добавку к кофе:'))
userCoffee.show_my_drink()