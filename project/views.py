from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import product

def home(request):
    products = product.objects.all().order_by('-created_at')  # optional ordering
    return render(request, 'products.html', {'products': products})
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
