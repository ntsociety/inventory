from select import select
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from . forms import OrderForm
from django.views.generic import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from .models import Order
from django.db.models import Q
from store.models import Customer, Product
#excel export
import pandas as pd
from django.http import HttpResponse, JsonResponse
# Create your views here.

@login_required(login_url='user-login')
def create_order(request):
    product = Product.objects.all()
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            status = form.cleaned_data['status']
            order = Order.objects.create(customer=customer, product=product, quantity=quantity, status=status)
            order.user = request.user
            order.save()
            # Reduce the quantity of the sold products
            order_items = Order.objects.get(id=order.id)
            order_items.subtotal = 0
            order_items.subtotal += order_items.quantity
            #print(order_items.product.id)
            product = Product.objects.get(id=order_items.product.id)
            product.stock -= order_items.quantity
            product.sell += order_items.quantity
            product.save()
            messages.success(request, 'Commande enregistré avec succès !')
            return redirect('order')
    context = {
        'product': product,
        'form': form
    }
    return render(request, 'orders/create_order.html', context)

#create orders
@login_required(login_url='user-login') 
def addCart(request):
    product = Product.objects.filter(user=request.user)
    customer = Customer.objects.filter(user=request.user)
    for p in product:
        pass
        #print(p.product_name)
    for c in customer:
        pass
        #print(c.first_name)
    order = Order.objects.all()
    
    if request.method == 'POST':
        product = Product.objects.filter(user=request.user).get(product_name=request.POST['product'])
        customer = Customer.objects.filter(user=request.user).get(first_name=request.POST['customer'])
        quantity = request.POST['quantity']
        status = request.POST['status']
        order = Order.objects.create(product=product, customer=customer, quantity=quantity, status=status)
        order.product_name = product.product_name
        order.customer_name = customer.first_name
        print(order.product_name)
        print(order.customer_name)
        order.user = request.user
        order.save()
        
        # Reduce the quantity of the sold products
        order_items = Order.objects.get(id=order.id)
        order_items.subtotal = 0
        order_items.subtotal += order_items.quantity
        #print(order_items.product.id)
        product = Product.objects.get(id=order_items.product.id)
        product.stock -= order_items.quantity
        product.sell += order_items.quantity
        product.save()
        messages.success(request, 'Commande enregistré avec succès !')
        return redirect('order')
    
    
    context = {
        'customer': customer,
        'product': product,
    }
    return render(request, 'orders/add_cart.html', context)


@login_required(login_url='user-login')
def order(request):
    order = Order.objects.filter(user=request.user).order_by('-created_date')
    for o in order:
        print(o.sub_total)
    order_count = order.count()
    paginator = Paginator(order, 4)
    page = request.GET.get('page')
    paged_orders = paginator.get_page(page)
    context = {
        'order_count': order_count,
        'order': paged_orders
    }
    return render(request, 'orders/order.html', context)

# class OrderListView(ListView):
#     model = Order
#     template_name = 'orders/order.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['order'] = Order.objects.all().order_by('-id')
#         return context

@login_required(login_url='user-login') 
def order_detail(request, pk):
    single_order = Order.objects.filter(user=request.user).get(id=pk)
    context = {
        'single_order': single_order
    }
    return render(request, 'orders/order_detail.html', context)


@login_required(login_url='user-login')
def edit_order(request, pk):
    item = Order.objects.filter(user=request.user).get(id=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Commande modifié avec succès !')
            return redirect('order')
    else:
        form = OrderForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'orders/edit_order.html', context)


@login_required(login_url='user-login')
def order_delete(request, pk):
    item = get_object_or_404(Order, id=pk)
    item.delete()
    messages.success(request, 'Commande supprimé avec succès !')
    return redirect('order')

# def customer_detail(request, pk):
#     single_customer = Customer.objects.get(order_id=pk)
#     context = {
#         'single_customer': single_customer
#     }
#     return render(request, 'store/customer/customer_detail.html', context)

#search orders
def search_order(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            order = Order.objects.order_by('-created_date').filter(Q(customer_name__icontains=keyword) | Q(product_name__icontains=keyword), user=request.user)
            order_count = order.count()
    context = {
        'order': order,
        'order_count': order_count,
    }
    return render(request, 'orders/order.html', context)



#export data to excel

def export_data_order(request):
    orders = Order.objects.filter(user=request.user)
    data = []
    for order in orders:
        msg = "Commandes exportés avec succès, stocké dans le dossier commande"
        order.sub_total = order.quantity * order.product.price
        data.append({
               "nom":     order.product, 
                "Client":    order.customer,
                "Prix Unitaire" : order.product.price,
                "Quantité": order.quantity,
                "Prix Total" : order.sub_total, 
                "Status" : order.status,  
                #"Date" : order.created_date, 
        }) 
    pd.DataFrame(data).to_excel('commande/commandes.xlsx')
    messages.success(request, msg)
    return redirect('order')