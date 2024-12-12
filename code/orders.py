class IceStorm:
    _valid_flavors = {
        "mint chocolate chip": 4.0,
        "chocolate": 3.0,
        "vanilla bean": 3.0,
        "banana": 3.5,
        "butter pecan": 3.5,
        "s'more": 4.0
    }

    _valid_mixins = {
        "cherry": 0.0,
        "whipped cream": 0.0,
        "caramel sauce": 0.5,
        "chocolate sauce": 0.5,
        "storios": 1.0,
        "dig dogs": 1.0,
        "T&Ts": 1.0,
        "cookie dough": 1.0,
        "pecans": 0.5
    }

    def __init__(self):
        self._price = 0.0
        self._flavor = None
        self._mixins = set()

    def get_flavor(self):
        "flavor getter"
        return self._flavor

    def get_mixins(self):
        "mixins getter"
        return self._mixins

    def count_mixins(self):
        "returns the length of the mixins attribute"
        return len(self._mixins)

    def get_total(self):
        "price getter"
        return self._price

    def set_flavor(self, flavor):
        "changes or establishes the flavor of the ice cream"
        # checks if the flavor is valid, sets the flavor, then sets the price.
        if flavor in self._valid_flavors:
            self._flavor = flavor
            self._price = self._valid_flavors[flavor]
        else:
            raise ValueError(f"Invalid, choose a flavor from {
                self._valid_flavors}")

    def add_mixin(self, mixin):
        "appends the mixins list with the given argument"
        # checks if the mixin is valid, adds it to the mixins list, and adds the price.
        if mixin in self._valid_mixins:
            self._mixins.add(mixin)
            self._price += self._valid_mixins[mixin]
        else:
            raise ValueError(f"Invalid, choose a mixin from {
                self._valid_mixins}")

    def set_mixins(self, new_list):
        "add multiple mixins at a time"
        for topping in new_list:  # iterates through the list of new mixins
            if topping not in self._valid_mixins:  # checks if each mixin is valid
                raise ValueError(f"Invalid, choose a mixin from {
                                 self._valid_mixins}")
        # removes any mixins already in the instance
        self._price = self._valid_flavors[self.get_flavor()]
        self._mixins = set()
        for new in new_list:
            self.add_mixin(new)


class Food:
    _valid_foods = {
        "hotdog": 2.3,
        "corndog": 2.0,
        "ice cream": 3.0,
        "onion rings": 1.75,
        "french fries": 1.5,
        "tater tots": 1.7,
        "nacho chips": 1.9
    }

    _valid_toppings = {
        "cherry": 0.0,
        "whipped cream": 0.0,
        "caramel sauce": 0.5,
        "chocolate sauce": 0.5,
        "nacho cheese": 0.3,
        "chili": 0.6,
        "bacon bits": 0.3,
        "ketchup": 0.0,
        "mustard": 0.0
    }

    def __init__(self, food):
        self._price = 0.0
        self._food = self.set_food(food)
        self._toppings = set()

    def get_food(self):
        "getter for the food attribute"
        return self._food

    def get_total(self):
        "getter for the price"
        return round(self._price, 2)

    def get_toppings(self):
        "getter for the toppings list"
        return self._toppings

    def count_toppings(self):
        "returns the number of toppings applied to the order"
        return len(self._toppings)

    def set_food(self, order):
        "sets or changes the _food attribute to the inputted value"
        if order in self._valid_foods:  # checks if the food is in the list of valid orders
            self._food = order
            self._price = self._valid_foods[order]
            return order
        else:
            raise ValueError(f"Invalid, pick an item from {self._valid_foods}")

    def add_topping(self, topping):
        "adds a topping to the instance"
        if topping in self._valid_toppings:  # checks if the topping is in the list of valid toppings
            if topping not in self._toppings:  # checks if the topping is not already in the instance
                self._toppings.add(topping)
                self._price += self._valid_toppings[topping]
            else:
                raise ValueError("cannot add multiple of the same topping")
        else:
            raise ValueError(f"Invalid topping: choose one from {
                             self._valid_toppings}")

    def set_toppings(self, new_list):
        "allows for the addition of multiple toppings at once"
        for topping in new_list:  # iterates through the list of new toppings
            if topping not in self._valid_toppings:  # checks if each topping is valid
                raise ValueError(f"Pick a proper topping from {
                                 self._valid_toppings}")
        # removes any toppings already in the instance
        new_toppings = set(new_list) - self._toppings
        self._price = self._valid_foods[self.get_food()]
        for new in new_toppings:  # iterates though each new topping in the list
            self._price += self._valid_toppings[new]
        self._toppings = set(new_list)


class Drink:
    "takes a size argument with declaration. Attributes are base(str), flavors(set(str)), and size(str)"
    # define the list of bases and flavors
    _valid_bases = {"water", "sbrite", "pokecola",
                    "Mr.Salt", "hill fog", "leaf wine"}
    _valid_flavors = {"lemon", "cherry",
                      "strawberry", "mint", "blueberry", "lime"}
    _size_costs = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15

    }
    # variable initalizers

    def __init__(self, size):
        self._base = None
        self._flavors = set()
        self._size = None
        self._cost = 0.0
        self.set_size(size)

    # attaches the value of the base to the get_base method
    def get_size(self):
        "getter function. Returns the local _size attribute"
        return self._size

    def get_base(self):
        "getter function. Returns the local _base attribute"
        return self._base

    # does the same here
    def get_flavors(self):
        "getter function. Returns the local _flavors attribute"
        return list(self._flavors)

    # does the same here
    def get_num_flavors(self):
        "reports the length of the _flavors set."
        return len(self._flavors)

    def get_total(self):
        "getter function. returns the local _cost attribute"
        return self._cost

    # first checks if the inputted base value is a valid base, and sets the value of the base field to the value in the argument
    def set_base(self, base):
        "takes a string as an argument. changes or defines the base attribute of the object if it is one of a predetermined list"
        if base in self._valid_bases:
            self._base = base
        else:
            raise ValueError(f"Pick a proper base from {self._valid_bases}.")

    # first checks if the value is valid, then adds it to a list
    def add_flavor(self, flavor):
        "takes a string as an argument. appends a flavor to the _flavors set attribute if it is one of a predetermined list"
        if flavor in self._valid_flavors:
            if flavor not in self._flavors:
                self._cost += 0.15
            self._flavors.add(flavor)
        else:
            raise ValueError(f"Pick a proper flavor from {
                             self._valid_flavors}")

    # attaches the value of the list to the actual flavors field accessable outside the object
    def set_flavors(self, flavors):
        "takes a set(str) as an argument. changes the _flavors list to the one inputted in the method"
        for flavor in flavors:
            if flavor not in self._valid_flavors:
                raise ValueError(f"Pick a proper flavor from {
                                 self._valid_flavors}")
        new_flavors = set(flavors) - self._flavors
        self._cost += 0.15 * len(new_flavors)
        self._flavors = set(flavors)

    def set_size(self, size):
        "takes a string as an argument. defines or changes the _size attribute to the inputted argument"
        size = size.lower()
        if size in self._size_costs:
            self._size = size
            self._cost = self._size_costs[size] + 0.15 * len(self._flavors)
        else:
            raise ValueError(f"Invalid size: {size} Pick a proper size from list {
                             list(self._size_costs.keys())}")


class Order:
    "takes no arguments to create an instance. Attributes are _items(list(Drink)), and _tax_rate(double)"
    _tax_rate = 0.0725
    # initializing lists

    def __init__(self):
        self._items = []

    # attaches the list to a globally accessable method
    def get_items(self):
        "getter function. reports the list in the _items attribute"
        return self._items

    def get_total(self):
        "getter function. Returns the total cost of every drink in the _items list"
        return sum(drink.get_total() for drink in self._items)

    def get_num_items(self):
        "Returns the length of the _items list"
        return len(self._items)

    def get_tax(self):
        "Calculates and returns the taxes of the order"
        return self.get_total() * 1 + self._tax_rate

    # creates a formatted list of all the Drink objects in the items list
    def get_receipt(self):
        "returns a dictionary showing the number of items in the _items list, each item in the _items list, the subtotal, taxes, and grand total of the order"
        receipt_data = {
            "number_items": self.get_num_items(),
            "drinks": [],
            "food": [],
            "icestorm": [],
            "subtotal": self.get_total(),
            "taxes": self.get_total() * self._tax_rate,
            "grand_total": self.get_tax()
        }

        for i, item in enumerate(self._items):
            if isinstance(item, Drink):
                drink_data = {
                    "number_items": i + 1,
                    "base": item.get_base(),
                    "size": item.get_size(),
                    "flavors": item.get_flavors(),
                    "total_cost": item.get_total()
                }
                receipt_data["drinks"].append(drink_data)
            if isinstance(item, Food):
                food_data = {
                    "number_items": i + 1,
                    "order": item.get_food(),
                    "toppings": item.get_toppings(),
                    "total_cost": item.get_total()
                }
                receipt_data["food"].append(food_data)
            if isinstance(item, IceStorm):
                ice_storm_data = {
                    "number items": i + 1,
                    "flavor": item.get_flavor(),
                    "mixins": item.get_mixins(),
                    "total_cost": item.get_total()
                }
                receipt_data["icestorm"].append(ice_storm_data)

#            base = drink.get_base()
#            flavors = ", ".join(drink.get_flavors())
#            receipt += f"{i + 1}: base - {base}, flavors - {flavors}\n"
        return receipt_data

    # Checks if the inputted argument is of the Drink class, then adds it to the items list
    def add_item(self, item):
        "takes a Drink object as an argument. adds the inputted argument to the _items list"
        if isinstance(item, Drink):
            self._items.append(item)
        elif isinstance(item, Food):
            self._items.append(item)
        elif isinstance(item, IceStorm):
            self._items.append(item)
        else:
            raise ValueError("you can only add drinks or food to this order")

    # checks if the chosen index is inside the list, then removes it from the list
    def remove_item(self, index):
        "takes an int as an argument. Removes the selected item from the _items list"
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            raise IndexError("Invalid, cannot remove")
