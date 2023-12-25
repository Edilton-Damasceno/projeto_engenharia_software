class Sujeito:
    def __init__(self):
        self._observadores = []

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self, mensagem):
        for observador in self._observadores:
            observador.update(mensagem)
            observador.set_count_notificacao()
