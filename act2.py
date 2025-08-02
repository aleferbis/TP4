import json

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class Envio:
    def __init__(self, costo, tiempo_entrega):
        self.costo = costo
        self.tiempo_entrega = tiempo_entrega

    def calcular_costo(self):
        return self.costo

    def obtener_tiempo(self):
        return self.tiempo_entrega

    def __str__(self):
        return f"Costo: ${self.costo}, Tiempo estimado: {self.tiempo_entrega}"

class EnvioEstandar(Envio):
    def __init__(self):
        super().__init__(costo=5, tiempo_entrega="5-7 días hábiles")


class EnvioExpress(Envio):
    def __init__(self):
        super().__init__(costo=15, tiempo_entrega="1-2 días hábiles")


class EnvioPersonalizado(Envio):
    def __init__(self, distancia_km):
        costo = 2 * distancia_km
        super().__init__(costo=costo, tiempo_entrega=f"{1 + distancia_km//50} días aprox.")

class Pedido:
    def __init__(self, producto, metodo_envio):
        self.producto = producto
        self.metodo_envio = metodo_envio

    def calcular_total(self):
        return self.producto.precio + self.metodo_envio.calcular_costo()

    def __str__(self):
        return f"Producto: {self.producto.nombre}, Precio: ${self.producto.precio}, " \
               f"Envío: {self.metodo_envio.costo}, Total: ${self.calcular_total()}, " \
               f"Tiempo de entrega: {self.metodo_envio.tiempo_entrega}"

    @staticmethod
    def guardar_pedido(pedido, archivo="pedidos.json"):
        data = {
            "producto": pedido.producto.nombre,
            "precio_producto": pedido.producto.precio,
            "costo_envio": pedido.metodo_envio.costo,
            "total": pedido.calcular_total(),
            "tiempo_entrega": pedido.metodo_envio.tiempo_entrega
        }
        try:
            with open(archivo, "r") as f:
                pedidos = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pedidos = []

        pedidos.append(data)

        with open(archivo, "w") as f:
            json.dump(pedidos, f, indent=4)

p1 = Producto("Teclado mecánico", 50)
p2 = Producto("Auriculares", 30)

pedido1 = Pedido(p1, EnvioEstandar())
pedido2 = Pedido(p2, EnvioExpress())
pedido3 = Pedido(p1, EnvioPersonalizado(distancia_km=20))

print(pedido1)
print(pedido2)
print(pedido3)

Pedido.guardar_pedido(pedido1)
Pedido.guardar_pedido(pedido2)
Pedido.guardar_pedido(pedido3)
