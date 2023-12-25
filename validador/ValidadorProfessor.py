from validador import IValidador

class ValidadorProfessor(IValidador.IValidador):
    def __init__(self, usuario, livro):
        super().__init__(usuario, livro)
        self.livro = livro
        self.usuario = usuario

    def validar(self):

        # (i)Se o livro está disponivel.
        if self.disponibilidade(self.livro):
            pass
        else:
            return 'O livro não está disponivel'

        # (ii) Se o usuario deve livro
        if self.devedor(self.usuario):
            pass
        else:
            return 'O usuario deve livro'

    def devedor(self, usuario):
        return usuario.get_devedor()

    def disponibilidade(self, livro):
        for exemplar in livro.exemplares:
            if exemplar.disponivel:
                return True
        return False

