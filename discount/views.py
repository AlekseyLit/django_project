from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {"message": 'уже не привет!'})


def discounts_list(request):
    pass