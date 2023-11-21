from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Category, UserCategory
from .forms import UserCategoryForm


def index(request):
    user_category = UserCategory.objects.all()
    return render(request, template_name='consumption/index.html', context=locals())


def detail_view(request, user_id):
    user = UserCategory.objects.get(pk=user_id)
    return render(request, 'consumption/detail.html', locals())



def choose_category(request):
    category_list = Category.objects.all()
    if request.method == "POST":
        form = UserCategoryForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            category = form.cleaned_data['my_category']
            UserCategory.objects.create(my_category=category, user=user)
        return redirect("consumption:index")
    else:
        form = UserCategoryForm()
    return render(request, template_name='consumption/category.html', context=locals())


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('consumption:index')
    else:
        form = UserCreationForm()
    return render(request, 'consumption/register.html', locals())

    #TCMLr6'8JYj.dcv
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('consumption:index')
    else:
        form = AuthenticationForm()
        ss = user = form.get_user()
    return render(request, 'consumption/a_form.html', locals())







