from django.shortcuts import render
from .models import *
from django.views.generic import ListView

fallacies = Fallacy.objects.all()

# def home(request):
#     fallacies = Fallacy.objects.all()
#     return render(request, 'fallacies/base.html', {'fallacies': fallacies, 'title': 'Логические ошибки'})

class Home(ListView):
    model = Fallacy
    template_name = 'fallacies/base.html'
    context_object_name = 'fallacies'


def show_fallacy(request, fallacy_id):
    fallacies = Fallacy.objects.all()
    fallacy = Fallacy.objects.get(pk=fallacy_id)
    if fallacy_id == 1:
        previous_fallacy = Fallacy.objects.get(pk=24)
    else:
        previous_fallacy = Fallacy.objects.get(pk=fallacy_id - 1)
    if fallacy_id == 24:
        next_fallacy = Fallacy.objects.get(pk=1)
    else:
        next_fallacy = Fallacy.objects.get(pk=fallacy_id + 1)
    return render(request, 'fallacies/fallacy.html', {'fallacies': fallacies, 'fallacy': fallacy, 'previous_fallacy': previous_fallacy, 'next_fallacy': next_fallacy})





