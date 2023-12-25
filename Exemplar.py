class Exemplar():
    def __init__(self, livro_id, exemplar_id):
        self.livro_id = livro_id
        self.exemplar_id = exemplar_id
        self.disponivel = True
        self.reservado = False

    def get_disponivel(self):
        return self.disponivel

    def set_disponivel(self, estado):
        self.disponivel = estado

    def get_id(self):
        return self.exemplar_id

    def get_reservado(self):
        return self.reservado

    def set_reservado(self, estado):
        return self.reservado