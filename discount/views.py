from django.shortcuts import render
from django.contrib.auth.models import User
from discount.models import Discounts, Categories, Offers


def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')


def login(request):
    return render(request, 'log-in.html', {'message': ""})


def check_user(request):
    login = request.POST['auth-login']
    password = request.POST['auth-password']
    users = User.objects.filter(username=login)
    if len(users)> 0:
        if users[0].check_password(password):
            return render(request, 'log-in.html', {'message': "Вы авторизировались"})

    return render(request, 'log-in.html', {'message': "Неправильный логин или пароль"})




def discounts(request):
    if request.method != 'POST':
        categories = Categories.objects.order_by('name')
        return render(request, 'discounts.html', {'categories': categories})
    else:
        list = Discounts.objects.filter(category_id__name=request.POST['category'])
        categories = Categories.objects.order_by('name')
        return render(request, 'discounts.html', {"list": list, 'categories': categories})


def offers(request):
    if request.method != 'POST':
        categories = Categories.objects.order_by('name')
        return render(request, 'offers.html', {'categories': categories})
    else:
        list = Offers.objects.filter(category_id__name=request.POST['category'])
        categories = Categories.objects.order_by('name')
        return render(request, 'offers.html', {"list": list, 'categories': categories})