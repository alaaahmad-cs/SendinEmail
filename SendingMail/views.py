from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import Email
from .forms import SEndEmail
from django.contrib import messages 
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    return HttpResponse("the mail is sending")

def welcome(request):
    return render(request, "email.html")

class CreateFormEmail(CreateView):
    model = Email
    form_class = SEndEmail
    template_name ="mail.html"

    def form_valid(self, form):

          name = form.cleaned_data['name']
          email = form.cleaned_data['email']
          to_email = form.cleaned_data['to_email']
          message = form.cleaned_data['message']

          return super().form_valid(form)
    
          send_mail(
                  subject = name,
                   message = message,
                   from_email = email,
                   recipient_list=[to_email],
                   fail_silently=False
                )
          return redirct('mail')
          message.success(request, ("the email is sending!!!"))   




# second way:  using methods to send mail:
# def send(request):
#   if request.method == "POST":
#       form = FormEmail(request.POST)
#       if form.is_valid():
#           subject = request.POST.get("name")
#           message = request.POST.get("message")
#           from_email = request.POST.get("email")
#           to_email = request.POST.get("to_email")
         
         
#           if subject and message and from_email and to_email:
#               try:
#                   send_mail(subject, message, from_email, [to_email])
#               except BadHeaderError:
#                   return HttpResponse("Invalid header found.")
#               return HttpResponseRedirect("/contact/thanks/")
#           else:
#                 return HttpResponse("all data sends")
#         # In reality we'd use a form class
#         # to get proper validation errors.
#   return render(request, "mail.html", {})