from .colors import *
from .pieces import *


class Picture:

  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for fila in self.img:
      espejo = ""
      for letra in fila:
        espejo = letra + espejo
      vertical.append(espejo)
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []

    for i in range(len(self.img)):
      l = len(self.img) - i - 1
      horizontal.append(self.img[l])

    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    new_img = []
    for string in self.img:
      new_string = [self._invColor(letter) for letter in string]
      new_img.append(new_string)
    print(new_img)
    return Picture(new_img)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    new_img = []
    l = max(len(self.img), len(p.img))

    for i in range(l):
      izquierda = self.img[i]
      derecha = p.img[i]
      if izquierda is None:
        izquierda = [" " for i in range(len(self.img[0]))]
      if derecha is None:
        derecha = [" " for i in range(len(p.img[0]))]
      row = izquierda + derecha
      new_img.append(row)

    return Picture(new_img)

  """ Devuelve una nueva figura poniendo la figura actual
      sobre la figura p """

  def up(self, p):
    new_img = self.img + p.img
    return Picture(new_img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura actual debajo
        de la figura p """
    new_img = p.img + self.img
    return Picture(new_img)

  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    new_img = []
    for row in self.img:
      new_row = row * n
      new_img.append(new_row)

    return Picture(new_img)

  def verticalRepeat(self, n):
    new_img = self.img * n
    return Picture(new_img)

  #Extra: Sólo para realmente viciosos
  def rotate_horario(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    transpuesta = list(zip(*self.img))

    rotada = [list(fila)[::-1] for fila in transpuesta]

    return Picture(rotada)
  
  def rotate_antihorario(self):
    return self.rotate_horario().rotate_horario().rotate_horario()
    

  @staticmethod
  def rock():
    return Picture(ROCK)

  @staticmethod
  def king():
    return Picture(KING)

  @staticmethod
  def bishop():
    return Picture(BISHOP)

  @staticmethod
  def square():
    return Picture(SQUARE)

  @staticmethod
  def knight():
    return Picture(KNIGHT)

  @staticmethod
  def pawn():
    return Picture(PAWN)

  @staticmethod
  def queen():
    return Picture(QUEEN)
