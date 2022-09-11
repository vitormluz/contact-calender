from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

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
