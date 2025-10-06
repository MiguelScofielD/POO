class Bike:
    def __init__(self, color, model, year, valor):
        self.color = color
        self.model = model
        self.year = year
        self.valor = valor

    def honk(self):
        print("Plim plim...")

    def stop(self):
        print("Stopping the bike ...")

    def run(self):
        print("Vrummmmmm ...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={valor}' for key, valor in self.__dict__.items()])}"


b2 = Bike("Yellow", "Monark", 2020, 800)

b2.honk()
b2.run()
b2.stop()
print(b2)
