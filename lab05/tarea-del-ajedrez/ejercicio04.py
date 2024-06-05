from chess.picture import Picture
from chess.interpreter import draw

patron = Picture.square().join(Picture.square().negative())

draw(patron)