from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from myapp.models import Profile


# Create your views here.

def about(request):
    return render(request, 'about.html')


def boots(request):
    return render(request, 'boots.html')


def django(request):
    return render(request, 'django.html')


def edu(request):
    return render(request, 'edu.html')


def flask(request):
    return render(request, 'flask.html')


def java(request):
    return render(request, 'java.html')


def python(request):
    return render(request, 'python.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():user = User.objects.get(username=username)
        if user.check_password(password):
            if user:
                auth.login(request,user)
                return redirect('dashboard')
            else:
                return render(request,'login.html')
        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html')


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            user_details = User.objects.get(id=user.id)
            profile_data = Profile.objects.filter(user_id=user.id)
        except User.DoesNotExist:
            user_details = None
            profile_data = None
    else:
        user_details = None
        profile_data = None

    return render(request, 'dashboard.html', {"user_details": user_details, 'profile_data': profile_data})
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email and password:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                # Redirect back to registration page if user or email already exists
                return redirect("register")
            else:
                # Create user if it doesn't exist
                user = User.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password
                )

                subject = "welcome to education"
                message = f"{user.first_name} {user.last_name},Thankyou for registering in education"
                email_from = settings.EMAIL_HOST_USER
                recipient_list=[user.email]
                send_mail(subject,message,email_from,recipient_list)



                # Create profile details for the user
                profile = Profile.objects.create(
                    user=user,
                    gender=request.POST.get("gender"),
                    course=request.POST.get("course")
                )

                # Redirect to login page after successful registration
                print('Registration successful. Redirecting to login...')
                return redirect("login")
        else:
            print('Email or password is empty. Rendering registration page...')
            return render(request, 'register.html')  # Render registration page with errors if email or password is empty

    else:
        # Render the registration form for GET requests
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect("edu")


