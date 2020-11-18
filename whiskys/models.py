from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Whisky(Base):
    nome = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Whisky"
        verbose_name_plural = "Whiskys"
    def __str__(self):
        return self.nome


class Avaliacao(Base):
    whisky = models.ForeignKey(Whisky, related_name='avaliacoes', on_delete=models.CASCADE)
    avaliador = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = "Avaliacao"
        verbose_name_plural = "Avaliacoes"
        unique_together = ['email', 'whisky']


    def __str__(self):
        return f'{self.avaliador} avaliou o curso {self.whisky} com nota {self.avaliacao}'