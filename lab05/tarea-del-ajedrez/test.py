from chess.picture import Picture
from chess.interpreter import draw

test = None
torre = Picture.rock()
caballo = Picture.knight()
rey = Picture.king()
dama = Picture.queen()
peon = Picture.pawn()


def test_invColor():
  global test
  test = torre.negative()


def test_espejos():
  global test
  test = torre.negative()
  torreHorizontal = torre.horizontalMirror()
  caballoVertical = caballo.verticalMirror()
  test = torreHorizontal


def test_join():
  global test
  test = torre.negative()
  pareja = rey.join(dama)
  test = pareja


def test_up():
  global test
  test = torre.negative()
  up = rey.up(peon)
  test = up


def test_under():
  global test
  test = torre.negative()
  under = dama.under(rey)
  test = under


def testHRepeat():
  global test
  test = torre.negative()
  fila = peon.horizontalRepeat(8)
  test = fila


def testVRepeat():
  global test
  test = torre.negative()
  columna = peon.verticalRepeat(8)
  test = columna


def test_rotateH():
  global test
  test = rey.rotate_horario()


def test_rotateA():
  global test
  test = rey.rotate_antihorario()


tests = [
    test_espejos, test_invColor, test_join, test_up, test_under, testHRepeat,
    testVRepeat, test_rotateH, test_rotateA
]

options = zip(tests, range(9))

print(list(options))

op = int(input("Elige el test a hacer: "))

tests[op]()
draw(test)
