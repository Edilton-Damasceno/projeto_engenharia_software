from abc import ABC, abstractmethod

class IValidador(ABC):
  def __init__(self, usuario, livro):
      pass

  #@abstractmethod
  def validar(self):
      pass

