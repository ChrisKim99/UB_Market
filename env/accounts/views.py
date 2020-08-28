from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utils import generate_token

# Create your views here.

def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST['username']
        password= request.POST["password"]
        confirm = request.POST["confirm password"]
        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            elif len(password) < 7:
                messages.info(request, 'Password is too short')
                return redirect('register')    
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.is_active =False
                user.save()
                current_site = get_current_site(request)
                subject ="Activate your Account"
                message =render_to_string('accounts/activate.html', 
                {
                    'user':user,
                    'domain':current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': generate_token.make_token(user)
                }
                )
                from_email = settings.EMAIL_HOST_USER
                to_list = [email]
                email = EmailMessage(
                    subject,
                    message, 
                    from_email, 
                    to_list
                    )
                email.send()
                messages.info(request,'User Created, Please check your email to verify')
        else:
            messages.info(request,'Password Not Matched')
            return redirect('register')
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def activate(request, uidb64, token):
    try:
        uid=force_text(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except Exception as identifier:
        user=None

    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.info(request, "account activated successfully")
        return redirect('login')  
    return render(request, 'accounts/activate_failed.html',status=401)  
