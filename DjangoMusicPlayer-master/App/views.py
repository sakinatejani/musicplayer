# from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Song
# imported our models
from django.core.paginator import Paginator

# from django.template.context import RequestContext

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about-us.html')


def contact(request):
    return render(request, 'contact-us.html')


def player(request):
    return render(request, 'web-player.html')


def added_player(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "player.html", context)






