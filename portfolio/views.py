from itertools import chain
from django.shortcuts import render, get_object_or_404
from .models import Portfolio , FAQ

def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)

    secoes = sorted(
        chain(
            portfolio.secoes_descritivas.all(),
            portfolio.secoes_carrosel.all(),
            portfolio.secoes_video.all(),
        ),
        key=lambda s: s.order,
    )

    secoes_context = [
        {
            "secao": secao,
            "tipo": secao.__class__.__name__,
        }
        for secao in secoes
    ]

    return render(
        request,
        'portfolio/detail.html',
        {
            'portfolio': portfolio,
            'secoes': secoes_context,
        }
    )

def portfolio_contato(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)

    return render(
        request,
        'portfolio/contato.html',
        {
            'portfolio': portfolio,
        }
    )


def portfolio_agenda(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)

    return render(
        request,
        'portfolio/agenda.html',
        {
            'portfolio': portfolio,
        }
    )


def portifolio_faq(request, portfolio_id):

    portfolio = Portfolio.objects.get(id=portfolio_id)

    # Recupera as perguntas frequentes associadas ao portfólio
    faqs = FAQ.objects.filter(portfolio=portfolio)

    return render(request, 'portfolio/faq.html', {
        'portfolio': portfolio,
        'faqs': faqs
    })

def portfolio_feedback(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    feedbacks = portfolio.feedbacks.all()
    return render(request, 'portfolio/feedback.html',
                  {'portfolio': portfolio,
                   'feedbacks': feedbacks})

