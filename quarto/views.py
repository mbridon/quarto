from django.http import HttpResponse
from django.views.generic import ListView, TemplateView

from .models import Player


class IndexView(TemplateView):    
    template_name = 'quarto/index.html'


class BoardView(TemplateView):
    template_name = 'quarto/board.html'
    context_object_name = 'board'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board'] = range(1, 17)


class PlayersView(ListView):
    context_object_name = 'players'

    def get_queryset(self):
        return Player.objects.all()
