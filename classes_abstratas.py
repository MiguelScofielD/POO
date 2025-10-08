from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("ligando a TV ...")
        print("Ligado!")

    def desligar(self):
        print("Desligando a TV ...")
        print("Deslidada!")


controle = ControleTV()
controle.ligar()
controle.desligar()
