from interface import IUsuario
from observer.Observador import Observador
from validador import ValidadorProfessor


class Professor(IUsuario.IUsuario, Observador):

  def __init__(self, codigo, nome):
    super().__init__()
    self.codigo = codigo
    self.nome = nome
    self.tempo_empretismo = 7
    self.emprestimos = []
    self.reservas = []
    self.devedor = False
    self.tempo_empretismo = 7
    self.count_notificacao = 0

  def set_count_notificacao(self):
    self.count_notificacao += 1

  def get_id(self):
    return self.codigo

  def validador(self, usuario, livro):
    return ValidadorProfessor.ValidadorProfessor(self, livro)

  def emprestimo(self, emprestimo, data_emprestimo):
    emprestimo.set_data_emprestimo(data_emprestimo)
    emprestimo.set_data_devolucao(data_emprestimo + self.tempo_empretismo)

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


  def RemoveReserva(self, livro):
    reserva = self.ObterReservaPorIdLivro(id)
    livro = reserva.get_livro()
    for reserva in self.reservas:
      if reserva.ObterLivroPorId(id) == livro:
        self.reservas.remove(reserva)
        return


  def devolucao(self, id):
    emprestimo = self.ObterEmprestimoPorIdLivro(id)
    livro = emprestimo.get_livro()
    return livro


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


  def update(self, mensagem):
    print(f"{self.nome} recebeu a mensagem: {mensagem}")

  def get_count_notificacao(self):
    return self.count_notificacao
