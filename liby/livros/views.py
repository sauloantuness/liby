from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import *
from .controllers import *

@login_required
def livros(request):
	context = {
		'livros' : Livro.objects.all(),
	}

	return render(request, 'livros/livros.html', context)

@login_required
def meusLivros(request):
	context = {
		'livros' : request.user.perfil.meusLivros(),
	}
	return render(request, 'livros/meus-livros.html', context)

@login_required
def adicionar(request):
	if request.method == 'POST':
		titulo = request.POST['titulo']
		autor = request.POST['autor']
		capa = request.POST['capa']
		descricao = request.POST['descricao']
		isbn = request.POST['isbn']
		edicao = request.POST['edicao']
		editora = request.POST['editora']
		estado = request.POST['estado']
		dono = request.user.perfil

		l = adicionarLivro(dono, titulo, autor, capa, descricao, isbn, edicao, editora, estado)

		return redirect('/livros/meus-livros/')

	return render(request, 'livros/adicionar.html')



@login_required
def buscar(request):
	if request.method == 'POST':
		titulo = request.POST['titulo']
		autor = request.POST['autor']

		context = {
			'livros' : buscarLivro(titulo, autor),
		}

		return render(request, 'livros/buscar.html', context)

	return render(request, 'livros/buscar.html')


@login_required
def livro(request, livro_id):
	context = {
		'livro' : Livro.objects.get(id=livro_id)
	}

	return render(request, 'livros/livro.html', context)

@login_required
def excluir(request, livro_id):
	Livro.objects.get(id=livro_id).delete()
	
	return redirect('/livros/meus-livros')


@login_required
def editar(request, livro_id):
	pass
