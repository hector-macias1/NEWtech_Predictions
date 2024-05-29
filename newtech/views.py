"""from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ItemForm, OutletForm, PredictionForm

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def add_new_sales(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        outlet_form = OutletForm(request.POST)
        if item_form.is_valid() and outlet_form.is_valid():
            item = item_form.save()
            outlet = outlet_form.save()
            # Create Sale object here if necessary
            return redirect('history')
    else:
        item_form = ItemForm()
        outlet_form = OutletForm()
    return render(request, 'addNewSales.html', {'item_form': item_form, 'outlet_form': outlet_form})

@login_required
def add_new_predictions(request):
    if request.method == 'POST':
        prediction_form = PredictionForm(request.POST)
        if prediction_form.is_valid():
            prediction_form.save()
            return redirect('history')
    else:
        prediction_form = PredictionForm()
    return render(request, 'addNewPredictions.html', {'prediction_form': prediction_form})

@login_required
def history(request):
    predictions = Prediction.objects.filter(user=request.user)
    return render(request, 'history.html', {'predictions': predictions})"""