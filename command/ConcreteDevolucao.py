from command.Command import Command
from Biblioteca import Biblioteca

class ConcreteDevolucao(Command):
  def execute(self, operando1, operando2):
    biblioteca = Biblioteca()
    print(biblioteca.devolucao(operando1, operando2))
