class Mano:
    def __init__(self, maxcapacity):
        self.maxcapacity = maxcapacity

    def puede_sostener(self, peso):
        return peso <= self.maxcapacity


class Persona:
    def __init__(self, fuerza_mano):
        self.mano_izquierda = Mano(fuerza_mano)
        self.mano_derecha = Mano(fuerza_mano)
        self.fuerza_total = fuerza_mano * 2

    def puede_levantar(self, peso):
        if self.mano_izquierda.puede_sostener(peso) or self.mano_derecha.puede_sostener(peso):
            return "Puede levantarlo con una sola mano"
        elif peso <= self.fuerza_total:
            return "Puede levantarlo usando ambas manos"
        else:
            return "No puede levantarlo"

Alejo = Persona(25)

print(Alejo.puede_levantar(20))
print(Alejo.puede_levantar(30))
print(Alejo.puede_levantar(50))
print(Alejo.puede_levantar(60))
