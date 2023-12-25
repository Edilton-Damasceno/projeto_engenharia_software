from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass
#Interface utilizada para a execução de diferentes comandos através do método execute()
#Será implementado nas classes/métodos concretos alusivo a cada comando