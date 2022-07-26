from django.shortcuts import render
from store.models import Product, Customer, Supplier
from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages

from store.views import customer, supplier



@login_required(login_url='user-login')
def dashboard(request):
    product = Product.objects.filter(user=request.user).order_by('-created_date')
    products = Product.objects.filter(user=request.user)
    paginator = Paginator(product, 10)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    total_product = product.count()
    #order
    order = Order.objects.filter(user=request.user).order_by('-created_date')
    paginator = Paginator(order, 10)
    page = request.GET.get('page')
    paged_orders = paginator.get_page(page)
    total_order = order.count()
    #customer
    customer = Customer.objects.filter(user=request.user)
    total_customer = customer.count()
    #supplier
    supplier = Supplier.objects.filter(user=request.user)
    total_supplier = supplier.count()
    
    
    #orders = Order.objects.all().order_by('-id')
    total_stock = 0
    for i in products:
        total_stock += (i.stock)
        
    context = {
        'total_stock': total_stock,
        'total_product': total_product,
        'product': paged_products,
        'supplier': total_supplier,
        'customer': total_customer,
        'total_order': total_order,
        'order': paged_orders
    }
    return render(request, 'index.html', context)
    return render(request, 'dashboard.html', context)

def home(request):
    products = Product.objects.filter(user=request.user)

    # Get the reviews
    # reviews = None
    # for product in products:
    #     reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        #'reviews': reviews,
    }
    return render(request, 'home.html', context)

