from validador import IValidador

class ValidadorAluno(IValidador.IValidador):
    def __init__(self, usuario, livro):
      super().__init__(usuario, livro)
      self.livro = livro
      self.usuario = usuario
      return

    def validar(self):

      # (i)Se o livro está disponivel ou foi reservado pelo usuario.
      if self.disponibilidade(self.livro):
        pass

      else:
        return '\nO livro não está disponivel', False

      # (ii) Se o usuario deve livro
      if not self.devedor(self.usuario):
        pass

      else:
        return '\nO usuario deve livro', False

      # (iii) Se o usuario não atingiu o limite de emprestimo
      if self.limiteEmprestimo(self.usuario):
        pass

      else:
        return '\nO usuario atingiu o limite de emprestimo', False

    # (iv) e (v) Se o limite de reservas não foi atingido ou que o usuario tenha uma reserva para o livro
      if self.limiteReservaLivro(self.livro, self.usuario):
        pass

      else:
        return '\nO limite de reservas foi atingido', False

      # (vi) Se o usuario já tem um emprestimo desse livro
      if self.primeiroEmprestimoLivro(self.livro, self.usuario):
        return 'Emprestimo permitido', True
      else:
        return '\nO usuario já tem um emprestimo desse livro', False
      
  
    def devedor(self, usuario):
      return usuario.get_devedor()

  
    def disponibilidade(self, livro):
      for exemplar in livro.exemplares:
          if exemplar.disponivel:
              return True
      return False


    def limiteReservaLivro(self, livro, usuario):
        exemplares = livro.get_exemplares()
        qtd = 0

        for exemplar in exemplares:
            if exemplar.get_reservado():
                qtd += 1
        if len(livro.get_exemplares())  > qtd:
            return True

        elif livro.get_id() in usuario.ListadeLivrosReserva():
            return True

        else:
            return False


    def limiteEmprestimo(self, usuario):
      emprestimos = usuario.emprestimos
      emprestimos_ativos = []

      for emprestimo in emprestimos:
          if emprestimo.get_status() == True:
            emprestimos_ativos.append(emprestimo)

      if len(emprestimos_ativos) < usuario.limite_emprestimo:
          return True
      else:
          return False


    def primeiroEmprestimoLivro(self, livro, usuario):
      livros_emprestados = usuario.ListaLivrosEmprestado()

      if livro.get_id() in livros_emprestados:
          return False
      else:
          return True
