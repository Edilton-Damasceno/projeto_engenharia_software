from observer.Sujeito import Sujeito
class Livro(Sujeito):
    def __init__(self, id, titulo, editora, autores, edicao, ano_publicacao, exemplares):
        self.id = id
        self.titulo = titulo
        self.editora = editora
        self.autores = autores
        self.edicao = edicao
        self.ano_publicacao = ano_publicacao
        self.exemplares = exemplares
        self.count_reserva = 0
        self._observadores = []

    # Métodos Get
    def get_id(self):
        return self.id

    def get_titulo(self):
        return self.titulo

    def get_editora(self):
        return self.editora

    def get_autores(self):
        return self.autores

    def get_edicao(self):
        return self.edicao

    def get_ano_publicacao(self):
        return self.ano_publicacao

    def get_exemplares(self):
        return self.exemplares


    # Métodos Set
    def set_id(self, novo_id):
        self.id = novo_id

    def set_titulo(self, novo_titulo):
        self.titulo = novo_titulo

    def set_editora(self, nova_editora):
        self.editora = nova_editora

    def set_autores(self, novos_autores):
        self.autores = novos_autores

    def set_edicao(self, nova_edicao):
        self.edicao = nova_edicao

    def set_ano_publicacao(self, novo_ano):
        self.ano_publicacao = novo_ano

    def set_count_reserva(self):
        self.count_reserva += 1

    def emprestar(self):
        for exemplar in self.exemplares:
            if exemplar.get_disponivel() == True:
                exemplar.set_disponivel(False)
                return

    def devolver(self):
        for exemplar in self.exemplares:
            if exemplar.get_disponivel() == False:
                exemplar.set_disponivel(True)
                return

    def obter_informacoes(self):
      return f"Título: {self.titulo}"

    def AddObservador(self, usuario):
        self.adicionar_observador(usuario)

    def VerificaQuantidadeReservas(self):
        if self.count_reserva >= 2:
            self.notificar_observadores(f'O livro {self.get_titulo()}, possui duas ou mais reservas.')


