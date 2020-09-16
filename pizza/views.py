from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewPizzaForm
from .models import Pizza
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = {'pizzas': Pizza.objects.all()}
    return render(request, 'pizza/index.html', context)

# Make pizza show route only accessible to logged in users
@login_required
def show(request, pizza_id):
    # Implicitely says that the first pizza in list has id of 1
    context = {'pizza': Pizza.objects.get(pk=pizza_id)}
    return render(request, 'pizza/show.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        pizza = NewPizzaForm(request.POST)
        if pizza.is_valid():
            pizza_id = pizza.save().id 
            return HttpResponseRedirect(f'/pizza/pizzas/{pizza_id}')
    else:
        form = NewPizzaForm()
    data = {'form': form}
    return render(request, 'pizza/new.html', data)

def handler404(request, exception):
    data = {'err': exception}
    return render(request, 'pizza/404.html', data)

def handler500(request):
    return render(request, 'pizza/500.html')