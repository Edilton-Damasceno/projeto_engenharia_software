import Emprestimo
import temporario_tabelas
import Reserva


# Implementação do design pattern Singleton e fachada

class Biblioteca():
    instance = None

    # Primeiro método a ser rodado na criação
    def __new__(cls):
        # cls é a própria classe
        if cls.instance is None:
            cls.instance = super(Biblioteca, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super().__init__()
        self.livros = temporario_tabelas.livros
        self.usuarios = temporario_tabelas.usuarios
        self.exemplares = temporario_tabelas.exemplares
        self.emprestimos = []
        self.reservas = []
        self._observadores = []

    def ObterUsuarioPorId(self, id):
        for usuario in self.usuarios:
            if usuario.get_id() == id:
                return usuario

    def ObterLivroPorId(self, id):
        for livro in self.livros:
            if livro.get_id() == id:
                return livro

    # Colocar marcação de tipo
    def emprestar_livro(self, usuario_id, livro_id):

        livro = self.ObterLivroPorId(livro_id)
        usuario = self.ObterUsuarioPorId(usuario_id)

        validador = usuario.validador(usuario, livro)

        validator_usuario = validador.validar()

        mensagem = validator_usuario[0]
        resultado = validator_usuario[1]

        if resultado == True:
            # Define o exemplar do livro como emprestado
            livro.emprestar()

            #  Cria uma intância de emprestimo
            emprestimo = Emprestimo.Emprestimo(usuario, livro)

            # Chama a função personalizada do usuario
            data = 10  # data aleatoria para testes
            usuario.emprestimo(emprestimo, data)

            self.emprestimos.append(emprestimo)
        return (mensagem)

    def reserva(self, usuario_id, livro_id):
        usuario = self.ObterUsuarioPorId(usuario_id)
        livro = self.ObterLivroPorId(livro_id)

        reserva = Reserva.Reserva(usuario, livro)

        data = 10  # data aleatoria para testes
        usuario.reserva(reserva, data)

        exemplares = livro.get_exemplares()

        for exemplar in exemplares:
            if exemplar.get_reservado() == False:
                exemplar.set_reservado = True
                break

        self.reservas.append(reserva)
        livro.set_count_reserva()
        livro.VerificaQuantidadeReservas()
        return f'\nSucesso! O usuario {usuario.get_nome()} reservou o livro {livro.get_titulo()}\n'

    def devolucao(self, usuario_id, livro_id):

        usuario = self.ObterUsuarioPorId(usuario_id)
        livro = self.ObterLivroPorId(livro_id)

        try:
            usuario.FinalizaEmprestimo(livro_id)
            livro.devolver()
            return f'Livro {livro.get_titulo()}, devolvido por {usuario.get_nome()}'

        except:
            return f'O usuario {usuario.get_nome()}, não possui um emprestimo do livro {livro.get_titulo()}'

    def QtdReservaLivro(self, livro_id):
        """Retorna a lista de usuarios que reservaram o livro"""
        info = ''
        qtd = 0

        for reserva in self.reservas:
            if reserva.ObterIdLivro() == livro_id:
                info += f'{reserva.get_nome_usuario()}\n'
                qtd += 1
        info += f'Quantidade de reservas: {qtd}'
        return info

    def InformacaoExemplarEmprestimo(self, livro_id):

        for emprestimo in self.emprestimos:
            if emprestimo.ObterIdLivro() == livro_id:
                usuario_id = emprestimo.ObterIdUsuario()
                usuario = self.ObterUsuarioPorId(usuario_id)

                if emprestimo.ObterIdUsuario() == usuario_id:
                    return f'usuario -> {usuario.get_nome()}     Data emprestimo -> {emprestimo.get_data_emprestimo()}     Data devolução -> {emprestimo.get_data_devolucao()}'

    ### TEM que terminar
    def ConsultaLivro(self, livro_id):
        livro = self.ObterLivroPorId(livro_id)
        reservas = self.QtdReservaLivro(livro_id)

        exemplares = livro.get_exemplares()
        msg = ''

        for exemplar in exemplares:
            info_exemplar = ''
            id = exemplar.get_id()
            disponivel = exemplar.get_disponivel()

            if disponivel == False:
                info_exemplar = f'\nInformação exemplar: {self.InformacaoExemplarEmprestimo(livro_id)}'
            msg += f'\nExemplares:\nCodigo do exemplar: {id}\nExemplar disponivel: {disponivel}{info_exemplar}\n\n'

        info = f'REERVAS: \nLivro: {livro.get_titulo()}\nReservado por: {reservas}\n {msg}'
        return info

    def ConsultaTransacoes(self, usuario_id):
        usuario = self.ObterUsuarioPorId(usuario_id)
        emprestimos = usuario.get_emprestimos()
        reservas = usuario.get_reservas()

        info_emprestiimo = ''
        info_reserva = ''

        for emprestimo in emprestimos:
            titulo = emprestimo.ObterTituloLivro()
            data = emprestimo.get_data_emprestimo()
            data_devolucao = emprestimo.get_data_devolucao()
            status = emprestimo.get_status()

            info_emprestiimo += f'\nTitulo: {titulo} * Data emprestimo: {data}  * Data devolução: {data_devolucao}  * Emprestimo ativo: {status}'

        for reserva in reservas:
            titulo = reserva.ObterTituloLivro()
            data = reserva.get_data_reserva()

            info_reserva += f'Titulo do livro: {titulo} * Data reserva: {data}'

        return f'\nEMPRESTIMOS:{info_emprestiimo}\n\nRESERVAS:\n{info_reserva}'

    def AddObservador(self, usuario_id, livro_id):
      usuario = self.ObterUsuarioPorId(usuario_id)
      livro = self.ObterLivroPorId(livro_id)
      livro.AddObservador(usuario)

    def QuantidadeNotificacao(self, usuario_id):
        usuario = self.ObterUsuarioPorId(usuario_id)
        return usuario.get_count_notificacao()


if __name__ == '__main__':
    bib = Biblioteca()

    bib.AddObservador(100, 100)

    print(bib.reserva(456, 100))
    print(bib.reserva(123, 100))

    print(bib.reserva(123, 400))
    print(bib.reserva(456, 400))

    # print(bib.ConsultaTransacoes(456))
    print(bib.ConsultaLivro(100))

    # print(bib.emprestar_livro(123, 100))
    # print(bib.emprestimos[0].get_livro().get_titulo())
    # print(bib.emprestimos[1].get_livro().get_titulo())

