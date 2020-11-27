from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import *
# from django.core.mail import send_mail, EmailMessage
# from django.conf import settings
# from .forms import EmailForm

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context data method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        return context

# def sendEmail(request):
#     subject = request.data['subject']
#     from_email = request.data['email']
#     message = request.data['message']
    
#     if subject and email and message is not None:
#         mail = send_mail(subject, message, from_email, recipient_list=[settings.EMAIL_HOST_USER],fail_silently=False)
#         mail.send()
#         return render(request, 'home')
#     else:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# # def send_mail(subject, message, from_email, recipient_list,
# #               fail_silently=False, auth_user=None, auth_password=None,
# #               connection=None, html_message=None):