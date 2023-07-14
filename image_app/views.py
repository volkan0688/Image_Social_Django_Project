from datetime import datetime
from unidecode import unidecode
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from .models import Image
from django.urls import reverse_lazy

import html

def list_image(request):
    all_images = Image.objects.all()
    image_dict = {"images": all_images, "active_page": "list_image"}
    return render(request, 'image_app/list_image.html', context=image_dict)

@login_required(login_url='/login')
def add_image(request):
    if request.method == 'POST':
        image = request.FILES.get("image")
        message = request.POST.get("message")
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Image.objects.create(username=request.user, image=image, message=message, tarih=tarih)
        return redirect('image_app:list_image')
    else:
        return render(request, 'image_app/add_image.html', {'active_page': 'add_image'})


def normalize_query(query):
    return unidecode(query)


def search_feature(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        normalized_query = html.unescape(search_query.lower())
        posts = Image.objects.filter(
            Q(message__icontains=normalized_query) |
            Q(username__username__icontains=normalized_query)
        )
        return render(request, 'image_app/search_results.html', {'query': search_query, 'posts': posts})
    else:
        return render(request, 'image_app/search_results.html', {})


@login_required
def delete_image(request, id):
    image = Image.objects.get(pk=id)
    if request.user == image.username:
        Image.objects.filter(id=id).delete()
        return redirect('image_app:list_image')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def login_view(request):
    return render(request, 'registration/login.html', {'active_page': 'login'})

@login_required
def logout_view(request):
    return redirect('image_app:list_image')

def signup_view(request):
    return render(request, 'registration/signup.html', {'active_page': 'signup'})
