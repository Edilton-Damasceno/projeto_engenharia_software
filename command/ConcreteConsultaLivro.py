from command.Command import Command
from Biblioteca import Biblioteca

class ConcreteConsultaLivro(Command):
  def execute(self, operando1):
    biblioteca = Biblioteca()
    print(biblioteca.ConsultaLivro(operando1))
