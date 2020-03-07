from django.db import models


class Type(models.Model):
    name = models.CharField(
        "Nombre",
        max_length=15,
        unique=True
    )

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return 'Tipo {name}'.format(
            name=self.name
        )


class Pokemon(models.Model):
    number = models.PositiveIntegerField(
        "Número",
        unique=True
    )
    name = models.CharField(
        "Nombre",
        max_length=30
    )
    height = models.FloatField(
        "Altura",
        null=True,
        blank=True
    )
    weight = models.FloatField(
        "Peso",
        null=True,
        blank=True
    )
    evolve_from = models.ForeignKey(
        "self",
        verbose_name="Forma Evolutiva",
        on_delete=models.CASCADE,
        related_name="evolve_to",
        null=True,
        blank=True
    )
    type_1 = models.ForeignKey(
        Type,
        verbose_name="Tipo 1",
        on_delete=models.PROTECT,
        related_name="pokemon_type_1"
    )
    type_2 = models.ForeignKey(
        Type,
        verbose_name="Tipo 2",
        on_delete=models.PROTECT,
        related_name="pokemon_type_2",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemon'

    def __str__(self):
        return '{number}: {name}'.format(
            number=self.number,
            name=self.name
        )
