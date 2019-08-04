import csv

class Pizza:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class Ordinary(Pizza):
    cost = 7.00

class NoGluten(Pizza):
    cost = 8.00

class WholeGrain(Pizza):
    cost = 9.00

# Decorator:
class Decorator(Pizza):
    def __init__(self, Pizza_x):
        self.component = Pizza_x
    def getTotalCost(self):
        return self.component.getTotalCost() + \
          Pizza.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + \
          ' ' + Pizza.getDescription(self)

class Cheese(Decorator):
    cost = 0.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class TomatoSauce(Decorator):
    cost = 0.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class Onion(Decorator):
    cost = 2.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class Mushrooms(Decorator):
    cost = 2.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class Olives(Decorator):
    cost = 2.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class SweetPotato(Decorator):
    cost = 3.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Agg(Decorator):
    cost = 3.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class ExtraCheese(Decorator):
    cost = 3.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

# -----------------------------------------------------

print("\n~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to PIZZA.PY!")
print("~~~~~~~~~~~~~~~~~~~~~~~\n")

food_menu = {1: Ordinary,
             2: NoGluten,
             3: WholeGrain,
             4: TomatoSauce,
             5: Cheese,
             6: ExtraCheese,
             7: Olives,
             8: Agg,
             9: Mushrooms,
             10: Onion,
             11: SweetPotato}

def order():
    # choose dough for the pizza:
    dough = int(input("What kind of dough do you want? "))
    x = 0
    while x == 0:
        if dough <= 3 and dough > 0:
            for i in food_menu:
                dough_x = food_menu[dough]()
                order = dough_x
                x = 1
        else:
            print("Try again. (choose 1-3)")
            dough = int(input("What kind of dough do you want? "))

    # if want topping - add
    Toppings = int(input("Toppings? if not choose 0: "))
    while Toppings != 0:
        count = 0
        for i in food_menu:
            if Toppings > 3 and Toppings == i:
                order = food_menu[Toppings](order)
            else:
                count += 1
        if count == 11:
            print("not found")

        Toppings = int(input("Toppings? if not choose 0: "))

    # print details:
    print("your Pizza: ", order.getDescription())
    cost_x = '$' + str(order.getTotalCost())
    print("cost: ", cost_x)

    # save dete in exel file:
    name = input("your name: ")
    ID = input("your ID: ")
    card_num = input("your credit card number: ")
    three_nums = input("three numbers behind the card: ")

    with open(r"C:\Users\גיתית\Desktop\PycharmProjects\Orders_file.csv", mode='a') as Orders_file:
        Orders_file = csv.writer(Orders_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        Orders_file.writerow([order.getDescription(), cost_x, name, ID, card_num, three_nums])

# for new order:
want_order_pizza = input("To order a Puzze - choose 1: ")
while want_order_pizza == '1':
    order()
    want_order_pizza = input("To add an order - choose 1: ")


print("fhjfryurkyktir")