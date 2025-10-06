# Herança múltipla


class A:
    pass


class B:
    pass


class C(A, B):
    pass


# Herança Simples


class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando Motor")


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    def __init__(self, modelo="Entrada", **kargs):
        super().__init__(**kargs)
        self.modelo = modelo


moto = Motocicleta("Preta", "abc-1234", 2)
moto.ligar_motor()


carro = Carro("hybrid", cor="Preto", placa="xqt-0034", numero_rodas=4)
carro.ligar_motor()
print(carro.modelo)
