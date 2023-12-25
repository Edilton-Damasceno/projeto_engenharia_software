from command.Command import Command
from Biblioteca import Biblioteca

class ConcreteEmprestarLivro(Command):
  def execute(self, operando1, operando2):
    biblioteca = Biblioteca()
    print(biblioteca.emprestar_livro(operando1, operando2))
