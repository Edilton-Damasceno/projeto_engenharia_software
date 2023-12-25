from command.Command import Command
from Biblioteca import Biblioteca

class ConcreteConsultaTransacoes(Command):
  def execute(self, operando1):
    biblioteca = Biblioteca()
    print(biblioteca.ConsultaTransacoes(operando1))
