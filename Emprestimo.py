class Emprestimo:
  def __init__(self, usuario, livro):
    self.usuario = usuario
    self.livro = livro
    self.data_emprestimo = None
    self.data_devolucao = None    
    self.status = False

  def set_usuario(self, usuario):
    self.usuario = usuario
    
  def set_livro(self, livro):
    self.livro = livro
    
  def set_data_emprestimo(self, data_emprestimo):
    self.data_emprestimo = data_emprestimo
  
  def set_data_devolucao(self, data_devolucao):
    self.data_devolucao = data_devolucao

  def set_status(self, status):
    self.status = status

  def get_data_emprestimo(self):
    return self.data_emprestimo

  def get_data_devolucao(self):
    return self.data_devolucao

  def get_status(self):
    return self.status


  def get_livro(self):
    return self.livro

  def ObterIdLivro(self):
    return self.livro.get_id()

  def ObterIdUsuario(self):
    return self.usuario.get_id()

  def ObterTituloLivro(self):
    return self.livro.get_titulo()