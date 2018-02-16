from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from system.forms import FeedbackForm
from solomon_catering.settings import EMAIL_HOST_USER


class HomeView(TemplateView):
    template_name = 'system/index.html'
    form = FeedbackForm()

    def get_context_data(self, **kwargs):
        return {'form':self.form}


def validate(name, phone_number):
    return len(name) > 0 and not name.isdigit() and len(phone_number) > 0


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('first_name')
        phone_number = request.POST.get('phone_number')
        sender = EMAIL_HOST_USER
        receiver = EMAIL_HOST_USER
        if validate(name,phone_number):
            text = name + ' ' + phone_number
            send_mail('New Client',text, sender,[receiver], fail_silently=True,)
            return render(request,'system/feedback.html',{'name':name, 'status':'OK'})
        return render(request, 'system/feedback.html', {'name': name})