from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from django.utils import translation
from django.views.generic import TemplateView

from system.forms import FeedbackForm


class HomeView(TemplateView):
    template_name = 'system/index.html'

    def get_context_data(self, **kwargs):
        form = FeedbackForm()
        if 'lang' in kwargs:
            pass
        return {'form':form}


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('first_name')
        phone_number = request.POST.get('phone_number')
        return HttpResponse("ok")
    return redirect(reverse('home'))
