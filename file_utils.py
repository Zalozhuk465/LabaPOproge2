import datetime
from models.Dish import Dish
from models.Drink import Drink
from models.Dessert import Dessert

def load_menu_from_file(filename):
    menu_items = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split("(")
            item_type = parts[0]
            values = parts[1].rstrip(")").split(", ")
            name = values[0][1:-1]  # Remove quotes
            price = float(values[1])
            prep_time = int(values[2])
            extra = True if len(values) < 4 else values[3] == "True"

            if item_type == "Dish":
                menu_items.append(Dish(name, price, prep_time, extra))
            elif item_type == "Drink":
                menu_items.append(Drink(name, price, prep_time, extra))
            elif item_type == "Dessert":
                menu_items.append(Dessert(name, price, prep_time, extra))
    return menu_items

def save_menu_to_file(menu_items, filename):
    with open(filename, "w") as file:
        for item in menu_items:
            file.write(f"{item.__class__.__name__}(\"{item.name}\", {item.price}, {item.preparation_time}, {getattr(item, 'is_vegetarian', getattr(item, 'is_alcoholic', getattr(item, 'contains_gluten', False)))})\n")