from django.shortcuts import render, get_object_or_404
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    context = {
        'contatos': contatos
    }
    return render(request, 'contatos/index.html', context)


def contato(request, contato_id):
    contatoo = get_object_or_404(Contato, id=contato_id)
    context = {
        'contato': contatoo
    }
    return render(request, 'contatos/contato.html', context)
