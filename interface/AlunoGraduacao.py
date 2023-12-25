from interface import IUsuario
from validador import ValidadorAluno


class AlunoGraduacao(IUsuario.IUsuario):
  def __init__(self, codigo, nome):
    super().__init__()
    self.codigo = codigo
    self.nome = nome
    self.emprestimos = []
    self.reservas = []
    self.devedor = False
    self.limite_emprestimo = 3
    self.tempo_empretismo = 3

    
  def get_id(self):
    return self.codigo

  def get_nome(self):
    return self.nome

  def get_emprestimos(self):
    return self.emprestimos

  def get_reservas(self):
    return self.reservas

  def get_devedor(self):
    return self.devedor

  def get_limite_emprestimo(self):
    return self.limite_emprestimo

  def validador(self, usuario, livro):
    return ValidadorAluno.ValidadorAluno(usuario, livro)


  def emprestimo(self, emprestimo, data_emprestimo):

    emprestimo.set_data_emprestimo(data_emprestimo)
    emprestimo.set_data_devolucao(data_emprestimo + self.tempo_empretismo)
    emprestimo.set_status(True)
    self.emprestimos.append(emprestimo)


  def ListaLivrosReserva(self):
    livros_reservados = []
    for reserva in self.reservas:
      livros_reservados.append(reserva.ObterIdLivro())
    return livros_reservados


  def ListaLivrosEmprestado(self):
    livros_emprestados = []
    for emprestimo in self.emprestimos:
      livros_emprestados.append(emprestimo.ObterIdLivro())
    return livros_emprestados


  def reserva(self, reserva, data_reserva):
    reserva.set_data_reserva(data_reserva)
    self.reservas.append(reserva)


  def ObterEmprestimoPorIdLivro(self, id):
    for emprestimo in self.emprestimos:
      if emprestimo.ObterIdLivro() == id:
        return emprestimo


  def ObterReservaPorIdLivro(self, id):
    for reserva in self.reservas:
      if reserva.ObterIdLivro() == id:
        return reserva      


  def FinalizaEmprestimo(self, livro_id):
    emprestimo = self.ObterEmprestimoPorIdLivro(livro_id)
    emprestimo.set_status(False)


