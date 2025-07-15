menu = {
    "Pizza Margarita": 8.99,
    "Hamburguesa Clasica": 5.99,
    "Ensalada Cesar": 7.5,
    "Agua Mineral": 1.5
}

def place_order(selected_food, money):
    try:
        print("\nMenú disponible:")
        for food, price in menu.items():
            print(f"{food}: {price} €")

        if selected_food not in menu:
            raise ValueError("El alimento seleccionado no está en el menú")

        price = menu[selected_food]
        if price > money:
            raise ValueError("No se disponen de suficientes fondos para realizar el pedido")

        total_price = price
        print(f"\n✅ Pedido realizado con éxito. Alimento seleccionado: {selected_food}, Total a pagar: {total_price} €")

    except ValueError as error:
        print(f"\n Error en el pedido: {error}")

alimento = input("Introduce el alimento que deseas pedir: ")
dinero = float(input("Introduce la cantidad de dinero que tienes: "))

place_order(alimento, dinero)