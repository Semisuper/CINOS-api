import orders
import pytest


def test_drink_getters():
    drink1 = orders.Drink("large")
    drink1.set_base("sbrite")
    drink1.set_flavors(["lemon", "cherry", "mint"])

    assert drink1.get_base() == "sbrite"
    assert drink1.get_flavors().__contains__("cherry")
    assert drink1.get_flavors().__contains__("mint")
    assert drink1.get_flavors().__contains__("lemon")
    assert drink1.get_num_flavors() == 3


def test_drink_cost():
    drink1 = orders.Drink("large")
    drink1.set_base("sbrite")
    drink1.set_flavors(["lemon", "cherry", "mint"])
    assert drink1.get_total() == 2.50


def test_base_error():
    with pytest.raises(ValueError) as excinfo:
        drink1 = orders.Drink("large")
        drink1.set_base("sprote")

    assert "Pick a proper base from" in str(excinfo.value)


def test_flavor_error():
    with pytest.raises(ValueError) as excinfo:
        drink1 = orders.Drink("large")
        drink1.set_base("sbrite")
        drink1.set_flavors(["grape", "cherry", "mint"])
    assert "Pick a proper flavor from" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        drink1 = orders.Drink("large")
        drink1.set_base("sbrite")
        drink1.add_flavor("grape")
    assert "Pick a proper flavor from" in str(excinfo.value)


def test_size_error():
    with pytest.raises(ValueError) as excinfo:
        drink1 = orders.Drink("large")
        drink1.set_size("beeg")
    assert "Invalid size:" in str(excinfo.value)


def test_single_flavor():
    drink1 = orders.Drink("large")
    drink1.set_base("sbrite")
    drink1.add_flavor("lemon")

    assert drink1.get_flavors() == ["lemon"]


def test_order_getters():
    drink1 = orders.Drink("large")
    drink1.set_base("sbrite")
    drink1.add_flavor("lemon")

    drink2 = orders.Drink("small")
    drink2.set_base("hill fog")
    drink2.add_flavor("strawberry")

    drink3 = orders.Drink("medium")
    drink3.set_base("pokecola")
    drink3.add_flavor("mint")

    order1 = orders.Order()
    order1.add_item(drink1)
    order1.add_item(drink2)
    order1.add_item(drink3)

    assert order1.get_items().__contains__(drink1)
    assert order1.get_items().__contains__(drink2)
    assert order1.get_items().__contains__(drink3)
    assert order1.get_total() == 5.75


def test_order_class():
    drink1 = orders.Drink("large")
    drink1.set_base("sbrite")
    drink1.add_flavor("lemon")

    drink2 = orders.Drink("small")
    drink2.set_base("hill fog")
    drink2.add_flavor("strawberry")

    drink3 = orders.Drink("medium")
    drink3.set_base("pokecola")
    drink3.add_flavor("mint")

    order1 = orders.Order()
    order1.add_item(drink1)
    order1.add_item(drink2)
    order1.add_item(drink3)
    assert order1.get_receipt().__contains__("number_items")


def test_order_errors():
    with pytest.raises(ValueError) as excinfo:
        drink1 = orders.Drink("large")
        drink1.set_base("sbrite")
        drink1.add_flavor("lemon")
        badobject = "drink"

        order1 = orders.Order()
        order1.add_item(drink1)
        order1.add_item(badobject)
    assert "you can only add drinks or food to this order" in str(
        excinfo.value)
    with pytest.raises(IndexError) as excinfo:
        drink1 = orders.Drink("large")
        drink1.set_base("sbrite")
        drink1.add_flavor("lemon")

        drink2 = orders.Drink("small")
        drink2.set_base("hill fog")
        drink2.add_flavor("strawberry")

        order2 = orders.Order()
        order2.add_item(drink1)
        order2.add_item(drink2)

        order2.remove_item(2)
    assert "Invalid, cannot remove" in str(excinfo.value)


def test_order_remove():
    drink1 = orders.Drink("large")
    drink1.set_base("sbrite")
    drink1.add_flavor("lemon")

    drink2 = orders.Drink("small")
    drink2.set_base("hill fog")
    drink2.add_flavor("strawberry")

    order1 = orders.Order()
    order1.add_item(drink1)
    order1.add_item(drink2)
    order1.remove_item(0)
    assert len(order1.get_items()) == 1


def test_food_order():
    food1 = orders.Food("hotdog")
    assert food1.get_food() == "hotdog"
    assert food1.get_total() == 2.3

    food1.add_topping("chili")
    assert food1.get_total() == 2.90
    assert food1.get_toppings() == {"chili"}


def test_food_advanced():
    food1 = orders.Food("hotdog")
    food1.set_toppings(["chili", "nacho cheese"])

    assert food1.get_toppings().__contains__("chili")
    assert food1.get_toppings().__contains__("nacho cheese")
    assert food1.get_total() == 3.2

    food1.set_toppings(["mustard", "ketchup"])
    assert food1.get_toppings().__contains__("mustard")
    assert food1.get_toppings().__contains__("ketchup")
    assert food1.get_total() == 2.3
    assert food1.count_toppings() == 2


def test_error_handling():
    with pytest.raises(ValueError) as excinfo:
        food1 = orders.Food("bologna")

    assert "Invalid, pick an item from" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        food1 = orders.Food("hotdog")
        food1.add_topping("chili")
        food1.add_topping("chili")

    assert "cannot add multiple of the same topping" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        food1.add_topping("cheese")

    assert "Invalid topping: choose one from" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        food1.set_toppings(["chili", "cheese"])

    assert "Pick a proper topping from" in str(excinfo.value)


def test_new_order():
    drink1 = orders.Drink("large")
    drink1.set_base("sbrite")
    drink1.add_flavor("lemon")

    drink2 = orders.Drink("small")
    drink2.set_base("hill fog")
    drink2.add_flavor("strawberry")

    drink3 = orders.Drink("medium")
    drink3.set_base("pokecola")
    drink3.add_flavor("mint")

    food1 = orders.Food("hotdog")
    food1.set_toppings(["chili", "nacho cheese"])

    food2 = orders.Food("corndog")
    food2.set_toppings(["mustard", "ketchup"])

    order1 = orders.Order()
    order1.add_item(drink1)
    order1.add_item(drink2)
    order1.add_item(drink3)
    order1.add_item(food1)
    order1.add_item(food2)
    assert order1.get_receipt().__contains__("number_items")


def test_icestorm_object():
    iceStorm1 = orders.IceStorm()
    iceStorm1.set_flavor("chocolate")
    iceStorm1.add_mixin("cherry")
    iceStorm1.set_mixins(["cherry", "whipped cream", "chocolate sauce"])

    assert iceStorm1.get_flavor() == "chocolate"
    assert iceStorm1.get_mixins() == {
        "cherry", "whipped cream", "chocolate sauce"}
    assert iceStorm1.count_mixins() == 3
    assert iceStorm1.get_total() == 3.5


def test_icestorm_errors():
    with pytest.raises(ValueError) as excinfo:
        iceStorm1 = orders.IceStorm()
        iceStorm1.set_flavor("strawberry")
    assert "Invalid, choose a flavor from" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        iceStorm1.set_flavor("chocolate")
        iceStorm1.add_mixin("M&Ms")
    assert "Invalid, choose a mixin from" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        iceStorm1.set_mixins(["cherry", "M&Ms"])

    assert "Invalid, choose a mixin from" in str(excinfo.value)


def test_icestorm_order():
    drink1 = orders.Drink("large")
    drink1.set_base("sbrite")
    drink1.add_flavor("lemon")

    drink2 = orders.Drink("small")
    drink2.set_base("hill fog")
    drink2.add_flavor("strawberry")

    drink3 = orders.Drink("medium")
    drink3.set_base("pokecola")
    drink3.add_flavor("mint")

    food1 = orders.Food("hotdog")
    food1.set_toppings(["chili", "nacho cheese"])

    food2 = orders.Food("corndog")
    food2.set_toppings(["mustard", "ketchup"])

    Icestorm1 = orders.IceStorm()
    Icestorm1.set_flavor("chocolate")
    Icestorm1.set_mixins(["cherry", "whipped cream", "chocolate sauce"])

    order1 = orders.Order()
    order1.add_item(drink1)
    order1.add_item(drink2)
    order1.add_item(drink3)
    order1.add_item(food1)
    order1.add_item(food2)
    order1.add_item(Icestorm1)
    assert order1.get_receipt().__contains__("number_items")
