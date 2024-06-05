from chess.picture import Picture
from chess.interpreter import draw

caballo = Picture.knight()
pareja = caballo.join(Picture.knight().negative())
pareja2 = caballo.negative().join(Picture.knight())
patron = pareja.up(pareja2)

draw(patron)
