from abc import ABC, abstractmethod

class IUsuario(ABC):
  def __init__(self):
      pass

  @abstractmethod
  def emprestimo(self, usuario, livro):
    pass

  @abstractmethod
  def reserva(self, reserva, data_reserva):
    pass

  def get_devedor(self):
    pass