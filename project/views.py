from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductForm

def home(request):
    return HttpResponse("Hello from core app!")
def homepage(request):
    return render(request, 'home.html')
# project/views.py

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # redirect to home or a success page
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
