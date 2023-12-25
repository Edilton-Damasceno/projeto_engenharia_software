#Classe voltada à entrada de dados. Uso do design pattern
#command
# Separarei o código em algumas responsabilidades: receiver (chamará a execução do comando de outras classes, involker (registra os comandos no dicionário e chama o execute), client (encarregado de pedir a execução do registro e da execução), concreteCommand (executa cada comando passando os operandos) 

from interface.Professor import Professor
from Biblioteca import Biblioteca
from command.LibInvoker import LibInvoker
from command.ConcreteEmprestarLivro import ConcreteEmprestarLivro
from command.ConcreteDevolucao import ConcreteDevolucao
from command.ConcreteReserva import ConcreteReserva
from command.ConcreteRegistrarObservador import ConcreteRegistrarObservador
from command.ConcreteConsultaLivro import ConcreteConsultaLivro
from command.ConcreteConsultaTransacoes import ConcreteConsultaTransacoes
from command.ConcreteQuantidadeNotificacoes import ConcreteQuantidadeNotificacoes
from command.ConcreteSai import ConcreteSai

# Este código de exemplo do padrão command é dividido em  partes:
# 1.classes externas (Avisa, Consulta, Lavanderia)
# 2. interface Command
# 4invoker(LibInvoker):cadastra comandos e chama a execucação genérica com argumentos
# 5 métodos concretos que implementam a interface command e tem o execute, que leva para o receiver
# 5. Receiver (CommandsReceiver): contém o execute e nele puxa o comando específico da classe externa
# 6. Cliente (executa a adição dos comandos) e Main (captura os comandos do teclado e manda executar)





# Cliente
biblioteca = Biblioteca()
novaBiblioteca = Biblioteca()
invocadorDeComandos = LibInvoker()

# Adicionando comandos ao dicionário
invocadorDeComandos.adicionarComando("emp", ConcreteEmprestarLivro())
invocadorDeComandos.adicionarComando("dev", ConcreteDevolucao())
invocadorDeComandos.adicionarComando("res", ConcreteReserva())
invocadorDeComandos.adicionarComando("obs", ConcreteRegistrarObservador())
invocadorDeComandos.adicionarComando("liv", ConcreteConsultaLivro())
invocadorDeComandos.adicionarComando("usu", ConcreteConsultaTransacoes())
invocadorDeComandos.adicionarComando("ntf", ConcreteQuantidadeNotificacoes())
invocadorDeComandos.adicionarComando("sai", ConcreteSai())


carlos = Professor(100, 'Carlos')
while True:
  # Entrada do usuário

  user_input = input("\nDigite o comando (por exemplo 'emp 123 100'): ")

  # A chamada da função 'consultar livro' está incorporada ao invocador
  partes = user_input.split()
  nome_comando = partes[0]
  invocadorDeComandos.executarComando(nome_comando, *map(int, partes[1:]))


  
