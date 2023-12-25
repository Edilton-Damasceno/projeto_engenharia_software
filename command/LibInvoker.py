class LibInvoker:
  def __init__(self):
    self.command_dict = {}
    # self.commands_receiver = commands_receiver

  def adicionarComando(self, nomeComando, valorComando):
    self.command_dict[nomeComando] = valorComando

  def executarComando(self, nomeComando, *args):
    valorComando = self.command_dict.get(nomeComando)
    if valorComando:
      valorComando.execute(*args)
    else:
      print("Comando não encontrado")

