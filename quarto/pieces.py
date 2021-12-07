from enums import Colors, Shapes, Sizes, Tops
from dataclasses import dataclass

__all__ = [
    "Colors", "Shapes", "Sizes", "Tops", "Piece"
]


played_pieces = []


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class Piece:
    color: Colors
    shape: Shapes
    size: Sizes
    top: Tops
