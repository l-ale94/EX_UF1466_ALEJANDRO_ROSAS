menu = {
    "pizza margarita": 8.99,
    "hamburguesa clasica": 5.99,
    "ensalada cesar": 7.5,
    "agua mineral": 1.5
}

# print(menu["Ensalada Cesar"])

def place_order(selected_food, money):
    pass
    
    if selected_food not in menu:
        raise ValueError("El alimento seleccionado no está en el menu")
    
