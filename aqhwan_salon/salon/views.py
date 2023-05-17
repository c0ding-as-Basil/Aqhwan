from django.shortcuts import render, get_object_or_404
from .models import Service
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Service, Comment
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'salon/home.html')


def contact(request):
    return render(request, 'salon/contact.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            login(request, user)
            return redirect('services')
    else:
        form = AuthenticationForm()
    return render(request, 'salon/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'salon/register.html', {'form': form})


def services(request):
    services = Service.objects.all()
    liked_services = request.user.liked_services.all(
    ) if request.user.is_authenticated else []
    return render(request, 'salon/services.html', {'services': services, 'liked_services': liked_services})


def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    liked_services = request.user.liked_services.all(
    ) if request.user.is_authenticated else []
    return render(request, 'salon/service_detail.html', {'service': service, 'liked_services': liked_services})


@login_required
def add_comment(request, service_id):
    if request.method == 'POST':
        comment_content = request.POST.get('comment')
        service = Service.objects.get(id=service_id)
        Comment.objects.create(
            service=service, user=request.user, content=comment_content)
    return redirect(f'services')


@login_required
def like_service(request, service_id):
    if request.method == 'POST':
        service = Service.objects.get(id=service_id)
        service.likes.add(request.user)
    return redirect('services')
