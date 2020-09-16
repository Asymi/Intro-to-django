from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.

def index(request):
    context = {'pizzas': Pizza.objects.all()}
    return render(request, 'pizza/index.html', context)

def show(request, pizza_id):
    # Implicitely says that the first pizza in list has id of 1
    context = {'pizza': Pizza.objects.get(pk=pizza_id)}
    return render(request, 'pizza/show.html', context)

def handle404(request, exception):
    return render(request, 'pizza/404.html')

def handle500(request):
    return render(request, 'pizza/500.html')