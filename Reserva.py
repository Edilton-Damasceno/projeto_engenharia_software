class Reserva:
  #Implementar padrão observer. A ideia é que  Toda vez que o livro tiver mais de duas 
  #reservas simultâneas, o livro deve “avisar” aos “observadores”. Ou seja, deve-se ter 
  #uma lista dos observadores e chamar um método para avisá-los toda vez que mais de duas 
  #reservas forem feitas. 
  
  def __init__(self, usuario, livro):
    self.usuario = usuario
    self.livro = livro
    self.data_reserva = None

  def get_livro(self):
    return self.livro

  def ObterIdLivro(self):
    return self.get_livro().get_id()

  def get_livro(self):
    return self.livro

  def get_usuario(self):
    return self.usuario

  def get_data_reserva(self):
    return self.data_reserva

  def ObterTituloLivro(self):
    return self.livro.get_titulo()

  def set_data_reserva(self, data_reserva):
    self.data_reserva = data_reserva

  def get_nome_usuario(self):
      return self.usuario.get_nome()

