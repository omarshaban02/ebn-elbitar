from managment.models import Product, Cart, Customers, Order
from django.shortcuts import render

def home(request):
    return render(request, 'store/home/home.html')

def customerProducts(request, catg):
    
    if catg == 'all':
       
       return render(request, 'store/home/customerProducts.html', {"products" : Product.objects.all()})
    context = {
        "products" : Product.objects.filter(category = catg),
    }

    return render(request, 'store/home/customerProducts.html', context)

def aboutUs(request):
    return render(request, 'store/aboutUs.html')

def product(request, product_id):
    product = Product.objects.get(id= product_id)
    category = product.category
    related_product = Product.objects.filter(category= category)
    context ={
        "product" : product,
        "related_product" : related_product[:4]
    }
    return render(request, 'store/home/productDetails.html', context)

def search(request):
    query = request.GET.get('query')
    searched_products = Product.objects.filter(name__icontains = query)
    context = {
        "searched_products" : searched_products,
        "query" : query,
        }
    return render(request, 'store/home/search.html', context)

def cart(request):

    return render(request, 'store/home/cart.html')

# def cart(request, customer_id):
#     customer = Customers.objects.get(id= customer_id)
#     context = {
#         "customer" : customer,

#     }
#     return render(request, 'store/home/cart.html', context)

def order(request):
    return render(request, 'thanks.html')