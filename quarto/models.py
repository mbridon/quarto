from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Piece(models.Model):
    size = models.PositiveSmallIntegerField(
        choices=(
            (1, 'small'),
            (2, 'tall'),
        )
    )
    color = models.PositiveSmallIntegerField(
        choices=(
            (1, 'black'),
            (2, 'white'),
        )
    )
    top = models.PositiveSmallIntegerField(
        choices=(
            (1, 'holed'),
            (2, 'fill'),
        )
    )
