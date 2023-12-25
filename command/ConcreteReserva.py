from command.Command import Command
from Biblioteca import Biblioteca

class ConcreteReserva(Command):
  def execute(self, operando1, operando2):
    biblioteca = Biblioteca()
    print(biblioteca.reserva(operando1, operando2))
