from command.Command import Command
from Biblioteca import Biblioteca

class ConcreteRegistrarObservador(Command):
  def execute(self, operando1, operando2):
    biblioteca = Biblioteca()
    biblioteca.AddObservador(operando1, operando2)