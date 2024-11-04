from django.core.mail import EmailMessage
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django import forms
from django.shortcuts import redirect, render
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages


def verify_email(request):
    if request.method == "POST":
        if request.user.email_is_verified != True:
            current_site = get_current_site(request)
            user = request.user
            email = request.user.email
            subject = "Verify Email"
            message = render_to_string('emailv/verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            return redirect('verify-email-done')
        else:
            return redirect('login')
    return render(request, 'emailv/verify_email.html')

def verify_email_done(request):
    return render(request, 'emailv/verify_email_done.html')


def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.email_is_verified = True
        user.save()
        messages.success(request, 'Your email has been verified.')
        return redirect('verify-email-complete')   
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'emailv/verify_email_confirm.html')



def verify_email_complete(request):
    return render(request, 'emailv/verify_email_complete.html')




class RegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


def registeration_view(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    
    else:
        form = RegisterationForm()

    return render(request, "registration/register.html", {"form": form})



def index(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "pages/profile.html")

            