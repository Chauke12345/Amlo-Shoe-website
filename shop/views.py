from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    products = Product.objects.filter(
        available=True
    ).order_by('-created_at')

    categories = Category.objects.all()

    women_category = categories.filter(slug='women').first()
    men_category = categories.filter(slug='men').first()
    kids_category = categories.filter(slug='kids').first()

    new_arrival = Product.objects.filter(
        available=True,
        new_arrival=True
    ).order_by('-created_at').first()

    return render(
        request,
        'shop/home.html',
        {
            'products': products,
            'categories': categories,
            'women_category': women_category,
            'men_category': men_category,
            'kids_category': kids_category,
            'new_arrival': new_arrival,
        }
    )

def product_detail(request, slug):
    product = get_object_or_404(
        Product,
        slug=slug,
        available=True
    )

    return render(
        request,
        'shop/product_detail.html',
        {'product': product}
    )


def cart(request):
    return render(
        request,
        'shop/cart.html'
    )


def category_products(request, slug):
    category = get_object_or_404(
        Category,
        slug=slug
    )

    products = Product.objects.filter(
        category=category,
        available=True
    ).order_by('-created_at')

    return render(
        request,
        'shop/category.html',
        {
            'category': category,
            'products': products
        }
    )
def size_guide(request):
    return render(request, 'shop/size_guide.html')
def contact(request):
    return render(request, 'shop/contact.html')

