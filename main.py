import tkinter as tk
from tkinter import ttk, messagebox
from file_utils import load_menu_from_file, save_menu_to_file
from models.Dish import Dish
from models.Drink import Drink
from models.Dessert import Dessert
import datetime

FILENAME = "menu"

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Menu Management")

        self.menu_items = load_menu_from_file(FILENAME)
        self.create_widgets()
        self.populate_table()

    def create_widgets(self):
        # Table
        columns = ("Type", "Name", "Price", "Preparation Time", "Special")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Entry section
        form = tk.Frame(self.root)
        form.pack(pady=10)

        self.type_var = tk.StringVar(value="Dish")
        self.name_var = tk.StringVar()
        self.price_var = tk.StringVar()
        self.prep_time_var = tk.StringVar()
        self.special_var = tk.BooleanVar(value=False)

        tk.Label(form, text="Type").grid(row=0, column=0)
        tk.OptionMenu(form, self.type_var, "Dish", "Drink", "Dessert").grid(row=0, column=1)

        tk.Label(form, text="Name").grid(row=0, column=2)
        tk.Entry(form, textvariable=self.name_var).grid(row=0, column=3)

        tk.Label(form, text="Price ($)").grid(row=0, column=4)
        tk.Entry(form, textvariable=self.price_var).grid(row=0, column=5)

        tk.Label(form, text="Prep Time (mins)").grid(row=0, column=6)
        tk.Entry(form, textvariable=self.prep_time_var).grid(row=0, column=7)

        tk.Checkbutton(form, text="Special", variable=self.special_var).grid(row=0, column=8)

        tk.Button(form, text="Add", command=self.add_item).grid(row=0, column=9)
        tk.Button(form, text="Delete Selected", command=self.delete_selected).grid(row=0, column=10)

    def populate_table(self):
        for item in self.menu_items:
            special_attr = ""
            if isinstance(item, Dish):
                special_attr = "Vegetarian" if item.is_vegetarian else ""
            elif isinstance(item, Drink):
                special_attr = "Alcoholic" if item.is_alcoholic else ""
            elif isinstance(item, Dessert):
                special_attr = "Gluten" if item.contains_gluten else ""
            
            self.tree.insert("", tk.END, values=(
                item.__class__.__name__, 
                item.name, 
                f"{item.price}$",
                f"{item.preparation_time} mins",
                special_attr
            ))

    def add_item(self):
        try:
            name = self.name_var.get()
            price = float(self.price_var.get())
            prep_time = int(self.prep_time_var.get())
            item_type = self.type_var.get()
            special = self.special_var.get()

            if item_type == "Dish":
                item = Dish(name, price, prep_time, special)
            elif item_type == "Drink":
                item = Drink(name, price, prep_time, special)
            elif item_type == "Dessert":
                item = Dessert(name, price, prep_time, special)
            else:
                raise ValueError("Invalid type")

            self.menu_items.append(item)
            self.tree.insert("", tk.END, values=(
                item_type, 
                name, 
                f"{price}$",
                f"{prep_time} mins",
                "Yes" if special else "No"
            ))
            save_menu_to_file(self.menu_items, FILENAME)

            self.name_var.set("")
            self.price_var.set("")
            self.prep_time_var.set("")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            return
        for item in selected:
            values = self.tree.item(item)["values"]
            for menu_item in self.menu_items:
                if (menu_item.__class__.__name__ == values[0] and 
                    menu_item.name == values[1] and 
                    menu_item.price == float(values[2][:-1]) and
                    menu_item.preparation_time == int(values[3].split()[0])):
                    self.menu_items.remove(menu_item)
                    break
            self.tree.delete(item)
        save_menu_to_file(self.menu_items, FILENAME)

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()