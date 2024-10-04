from django.db import models

class Produto(models.Model):
    codigoProduto = models.CharField(max_length=255)
    tituloProduto = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=2, decimal_places=1)
    descricao = models.TextField(max_length=255)
    imagemProduto = models.CharField(max_length=255)
    categoriaProduto = models.CharField(max_length=255)
    classProduto = models.DecimalField(max_digits=2, decimal_places=1)
    exibirHome = models.BooleanField(default=True)
