from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class HomePage(TemplateView):
    template_name = "home.html"

#
# def word_count(request):
#     return render(request, 'count.html')


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
