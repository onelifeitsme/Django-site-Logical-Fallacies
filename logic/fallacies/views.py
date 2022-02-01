from django.shortcuts import render
from .models import Fallacy
from django.views.generic import ListView

fallacies = Fallacy.objects.all()


class Home(ListView):
    """Представление главной страницы"""
    model = Fallacy
    template_name = 'fallacies/base.html'
    context_object_name = 'fallacies'


def show_fallacy(request, fallacy_id):
    """Представление страницы одной логической ошибки"""
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

    return render(request, 'fallacies/fallacy.html', {'fallacies': fallacies,
                                                      'fallacy': fallacy,
                                                      'previous_fallacy': previous_fallacy,
                                                      'next_fallacy': next_fallacy})
