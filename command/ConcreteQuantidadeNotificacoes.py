from command.Command import Command
from Biblioteca import Biblioteca

class ConcreteQuantidadeNotificacoes(Command):
  def execute(self, operando1):
    biblioteca = Biblioteca()
    print("O observador foi notificado: ", biblioteca.QuantidadeNotificacao(operando1), " vezes.\n")
