from django.core.mail import send_mail
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


def validate(name, phone_number):
    return len(name) > 0 and not name.isdigit() and len(phone_number) > 0


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('first_name')
        phone_number = request.POST.get('phone_number')
        sender = "quantagonista@gmail.com"
        receiver = "quantagonista@gmail.com"
        if validate(name,phone_number):
            text = name + ' ' + phone_number
            send_mail('New Client',text, sender,[receiver], fail_silently=True,)
            return render(request,'system/feedback.html',{'name':name, 'status':'OK'})
        return render(request, 'system/feedback.html', {'name': name})