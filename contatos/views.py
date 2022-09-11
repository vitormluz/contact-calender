from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Concat
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.http import Http404
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

    if not contatoo:
        raise Http404()

    context = {
        'contato': contatoo
    }
    return render(request, 'contatos/contato.html', context)


def busca(request):
    busca = request.GET.get('busca')

    if busca is None:
        raise Http404()

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        nome_completo__icontains=busca
    )

    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    context = {
        'contatos': contatos
    }
    return render(request, 'contatos/busca.html', context)
