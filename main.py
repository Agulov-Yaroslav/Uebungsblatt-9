#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Vorlage zu Übungsblatt 09"""


# # Alter Code, welcher durch die Pizza-Klasse ersetzt werden soll:
#
# def get_pizza_shape(pizza):
#     if isinstance(pizza["dimensions"], int):
#         pizza_shape = "circle"
#     else:
#         pizza_shape = "rectangle"
#     return pizza_shape
#
# def get_pizza_area(pizza):
#     pizza_shape = get_pizza_shape(pizza)
#     if pizza_shape == "circle":
#         pi = 3.1415
#         pizza_area = pi * (pizza["dimensions"] / 2) ** 2
#     if pizza_shape == "rectangle":
#         pizza_area = pizza["dimensions"][0] * pizza["dimensions"][1]
#     return pizza_area


class Pizza:
    """Eine Klasse zur Repräsentation einer Pizza mit verschiedenen Attributen und Methoden.

    Attribute:
        name (str): Der Name der Pizza.
        dimensions (int | tuple): Durchmesser der Pizza (falls kreisförmig)
        oder Seitenlängen (falls rechteckig).
        __toppings (list): Eine private Liste der Toppings
    """
    def __init__(self, name, dimensions):
        self.name = name
        self.dimensions = dimensions
        self.__toppings = []

    def shape(self):
        """
        :return:
        """
        if isinstance(self.dimensions, int):
            pizza_shape = "circle"
        else:
            pizza_shape = "rectangle"
        return pizza_shape

    def area(self):
        """

        :return:
        """
        if self.shape() == "circle":
            pi = 3.1415
            pizza_area = pi * (self.dimensions / 2) ** 2
        else:
            pizza_area = self.dimensions[0] * self.dimensions[1]

        return pizza_area

    def add_topping(self, topping):
        """

        :param topping:
        :return:
        """
        if isinstance(topping, Topping):
            self.__toppings.append(topping)
        else:
            raise TypeError(f"Bad topping, must be type 'Topping', not '{type(topping).__name__}'")

    def price(self):
        """

        :return:
        """
        grundpreis = self.area() * 0.005
        toppingspreis = sum(topping.price for topping in self.__toppings)
        return grundpreis + toppingspreis

class Topping:
    """
    Eine Klasse zur Repräsentation eines Pizza-Toppings.

    Attribute:
        name (str): Der Name des Toppings.
        price (float): Der Preis des Toppings in Euro.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == "__main__":

    # # Tests für Aufgabe 1
    # pizza_margherita = Pizza()
    # pizza_margherita.name = "Margherita"
    # pizza_margherita.dimensions = 28
    # pizza_hawaii = Pizza()
    # pizza_hawaii.name = "Hawaii"
    # pizza_hawaii.dimensions = (30, 40)
    # pizza_orders = [pizza_margherita, pizza_hawaii]
    # for i, pizza in enumerate(pizza_orders, start=1):
    #     print("Order", i, "is a Pizza", pizza.name)
    #     print("with a", pizza.shape(), "shape")
    #     print("and an area of", pizza.area(), "cm²")

    # # Tests für Aufgabe 2
    # pizza_margherita = Pizza("Margherita", 28)
    # pizza_hawaii = Pizza("Hawaii", (30, 40))
    # pizza_orders = [pizza_margherita, pizza_hawaii]
    # for i, pizza in enumerate(pizza_orders, start=1):
    #     print("Order", i, "is a Pizza", pizza.name)
    #     print("with a", pizza.shape(), "shape")
    #     print("and an area of", pizza.area(), "cm²")

    # # Tests für Aufgabe 3
    # pizza_hawaii = Pizza("Hawaii", 28)
    # extra_cheese = Topping("Extra Cheese", 0.5)
    # pineapple = Topping("Pineapple", 1)
    # pizza_hawaii.add_topping(extra_cheese)
    # pizza_hawaii.add_topping(pineapple)
    # try:
    #     not_a_topping = 1234
    #     pizza_hawaii.add_topping(not_a_topping)
    #     print("No TypeError detected")
    # except TypeError as e:
    #     print(f"TypeError detected: {e}")

    # Tests für Aufgabe 4
    custom_pizza = Pizza("Custom", (10, 20))
    print("The plain pizza slice costs", custom_pizza.price(), "€")
    a_few_olives = Topping("Olives", 0.75)
    some_artichokes = Topping("Artichokes", 1.5)
    custom_pizza.add_topping(a_few_olives)
    custom_pizza.add_topping(some_artichokes)
    custom_pizza.price()
    print("After adding the toppings, the pizza slice costs", custom_pizza.price(), "€")
