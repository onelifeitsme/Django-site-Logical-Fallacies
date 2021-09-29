from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return render(request, 'fallacies/base.html')

from fallacies.models import *
fallacies = Fallacy.objects.all()

def home(request):
    fallacies = Fallacy.objects.all()
    return render(request, 'fallacies/base.html', {'fallacies': fallacies, 'title': 'Логические ошибки'})

def about(request):
    return render(request, 'fallacies/about.html', {'title': 'О нас'})


def contact(request):
    return render(request, 'fallacies/contact.html', {'title': 'Связаться'})

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

def test(request):
    fallacy = fallacies[9]
    fallacy10 = fallacies[10]
    return render(request, 'fallacies/about.html', {'fallacy': fallacy, 'fallacy10': fallacy10})

def testus(request):
    return render(request, 'fallacies/test.html')




