from django.shortcuts import render
from acomapp.models import Category, Product

# Create your views here.
def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories':categories,
        'products':products
    }
    return render(request, 'base.html', context)
