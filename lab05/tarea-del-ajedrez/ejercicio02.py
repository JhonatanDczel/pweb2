from chess.picture import Picture
from chess.interpreter import draw

caballo = Picture.knight()
pareja = caballo.join(Picture.knight().negative())
patron = pareja.up(pareja.verticalMirror())

draw(patron)
