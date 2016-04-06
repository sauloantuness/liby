from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuario(models.Models):
	usuario = models.CharField(max_length=20)
	senha = models.CharField(max_length=50)
	email = models.EmailField()
	cidade = models.CharField(max_length=50)
	estado = models.CharField(max_length=2)
	foto = models.ImageField()

	def __str__(self):
		return self.usuario

class Livro(models.Models):
	ISBN = models.CharField(max_length=20)
	titulo = models.CharField(max_length=20)
	autor = models.CharField(max_length=20)
	edicao = models.CharField(max_length=20)
	dono = models.Foreign(Usuario)

	NOVO = '3'
	BOM = '2'
	RUIM = '1'

	ESTADO_OPCOES = (
		(NOVO,'novo'),
		(BOM,'bom'),
		(RUIM,'ruim')
	)

	estado = models.CharField(max_length=1,opcoes=ESTADO_OPCOES, default=BOM)

	def __str__(self):
		return self.titulo


class Mensagem(models.Models):
    data = models.DateField(auto_now_add=True)
    conteudo = models.TextField()
    destinatario = models.Foreign(Usuario)	 
    remetente = models.Foreign(Usuario)
    transacao = models.Foreign(Transacao)

	def __str__(self):
		return self.conteudo

class Transacao(models.Model):
	livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
	usuarioSolicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	concluida = models.BooleanField(default=False)
	avaliacaoDono = models.TextField()
	avaliacaoSolicitante = models.TextField()
	notaDono = models.IntegerField()
	notaSolicitante = models.IntegerField()