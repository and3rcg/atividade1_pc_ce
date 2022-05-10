from django.db import models

# as foreign keys não podem ser nulas


class Calibre(models.Model):
    desc_calibre = models.CharField(max_length=45)

    def __str__(self) -> str:
        return f'Calibre {self.desc_calibre}'


class ObjetoTipo(models.Model):
    tipo_de_objeto = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.tipo_de_objeto.title()}'


class Objeto(models.Model):
    objeto_tipo = models.ForeignKey(ObjetoTipo, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self) -> str:
        return f'Objeto ID {self.pk}: {self.objeto_tipo}'


class Arma(models.Model):
    id = models.OneToOneField(Objeto, on_delete=models.CASCADE, primary_key=True)
    calibre = models.ForeignKey(Calibre, on_delete=models.CASCADE, blank=False, null=False)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    quantidade_de_tiros = models.IntegerField()
    valor_estimado = models.FloatField()
    imagem = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self) -> str:
        return f'Arma {self.marca} {self.modelo}'


class Municao(models.Model):
    id = models.OneToOneField(Objeto, on_delete=models.CASCADE, primary_key=True)
    calibre = models.ForeignKey(Calibre, on_delete=models.CASCADE, blank=False, null=False)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    valor_estimado = models.FloatField()

    def __str__(self) -> str:
        return f'Munições {self.marca} {self.modelo}'
