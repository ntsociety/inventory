from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import AddStocks, Customer, Product, Supplier
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.db.models import Q
from django.template.defaultfilters import slugify
from category.models import Category
from .forms import Add_stockForm, supplierForm, ProductForm, customerForm
#excel export
import pandas as pd
from django.http import JsonResponse
# Create your views here.




#partie supplier
@login_required(login_url='user-login')
def create_supplier(request):
    form = supplierForm
    if request.method == 'POST':
        form = supplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fournisseur enregistré avec succès !')
            return redirect('supplier')
    else:
        form = supplierForm()
        context = {
            'form': form
        }
        
    return render(request, 'store/supplier/create_supplier.html', context)

@login_required(login_url='user-login')
def supplier(request):
    supplier = Supplier.objects.all()
    supplier_count = supplier.count()
    paginator = Paginator(supplier, 5)
    page = request.GET.get('page')
    paged_supplier = paginator.get_page(page)
    context = {
        'supplier_count': supplier_count,
        'supplier': paged_supplier
    }
    return render(request, 'store/supplier/supplier.html', context)

@login_required(login_url='user-login')
def supplier_detail(request, pk):
    single_supplier = Supplier.objects.get(id=pk)
    context = {
        'single_supplier': single_supplier
    }
    return render(request, 'store/supplier/supplier_detail.html', context)

@login_required(login_url='user-login')
def edit_supplier(request, pk):
    item = Supplier.objects.get(id=pk)
    if request.method == 'POST':
        form = supplierForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil modifié avec succès !')
            return redirect('supplier')
    else:
        form = supplierForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'store/supplier/edit_supplier.html', context)

@login_required(login_url='user-login')
def supplier_delete(request, pk):
    item = get_object_or_404(Supplier, id=pk)
    item.delete()
    messages.success(request, 'Profil supprimé avec succès !')
    return redirect('supplier')



#partie products
@login_required(login_url='user-login')
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # product_name = form.cleaned_data['product_name']
            # description = form.cleaned_data['description']
            # price = form.cleaned_data['price']
            # images = form.cleaned_data['images']
            # stock_initial = form.cleaned_data['stock_initial']
            # category = form.cleaned_data['category']
            # supplier = form.cleaned_data['supplier']
            #product = Product.objects.create(product_name=product_name, description=description, price=price, images=images, stock_initial=stock_initial, category=category, supplier=supplier)
            product = form.save()
            product = Product.objects.get(id=product.id)
            product.stock = product.stock_initial
            product.save()
            messages.success(request, 'Produit ajouté avec succès !')
            return redirect('product')
    else:
        form = ProductForm()
    context = {
        'form': form,
    }  
    return render(request, 'store/create_product.html', context)


@login_required(login_url='user-login')
def add_stock(request):
    form = Add_stockForm
    if request.method == 'POST':
        form = Add_stockForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            addstock = AddStocks.objects.create(product=product, quantity=quantity)
            addstock.save()
            addstock_items = AddStocks.objects.get(id=addstock.id)
            product = Product.objects.get(id=addstock_items.product.id)
            product.stock += addstock_items.quantity
            product.add_stock += addstock_items.quantity
            product.save()
            messages.success(request, 'Stock ajouté avec succès !')
            return redirect('product')
    else:
        form = Add_stockForm()
        context = {
            'form': form
        }  
    return render(request, 'store/add_stock.html', context)

@login_required(login_url='user-login')
def add_quantity(request):
    product = Product.objects.all()
    if request.method == 'POST':
        product = Product.objects.get(product_name=request.POST['product'])
        quantity = request.POST['quantity']
        add_stock = AddStocks.objects.create(product=product, quantity=quantity)
        add_stock.save()
        addstock = AddStocks.objects.create(product=product, quantity=quantity)
        addstock.save()
        addstock_items = AddStocks.objects.get(id=addstock.id)
        product = Product.objects.get(id=addstock_items.product.id)
        product.stock += addstock_items.quantity
        product.add_stock += addstock_items.quantity
        product.save()
        messages.success(request, 'Stock ajouté avec succès !')
        return redirect('product')
    
    context = {
        'product': product
    }  
    return render(request, 'store/add_quantity.html', context)


@login_required(login_url='user-login')
def product(request, category_slug = None):
    category = Category.objects.all()
    categories = None
    product = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        product = Product.objects.filter(category=categories)
        product_count = product.count()
        paginator = Paginator(product, 5)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    else:
        product = Product.objects.all().order_by('id')
        product_count = product.count()
        paginator = Paginator(product, 5)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    
    context = {
        'category': category,
        'product_count': product_count,
        #'paged_products': paged_products,
        'product': paged_products,
    }
    return render(request, 'store/product.html', context)

@login_required(login_url='user-login')
def product_detail(request, pk):
    single_product = Product.objects.get(id=pk)
    context = {
        'single_product': single_product
    }
    return render(request, 'store/products_detail.html', context)

@login_required(login_url='user-login')
def edit_product(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit modifié avec succès !')
            return redirect('product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'store/edit_product.html', context)


@login_required(login_url='user-login')
def product_delete(request, pk):
    item = get_object_or_404(Product, id=pk)
    item.delete()
    return redirect('product')


#search product
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            #product_count = product.count()
            product_count = product.count()
            #DataPribadiSiswa.objects.filter(siswa_kelas__some_name__icontains=keyword2))
    context = {
        'product': product,
        'product_count': product_count,
    }
    return render(request, 'store/product.html', context)


#partie custom
@login_required(login_url='user-login')
def create_customer(request):
    form = customerForm
    if request.method == 'POST':
        form = customerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client enregistré avec succès !')
            return redirect('customer')
    else:
        form = customerForm()
        context = {
            'form': form
        }  
    return render(request, 'store/customer/create_customer.html', context)

@login_required(login_url='user-login')
def customer(request):
    #total_prix = 0
    
    customer = Customer.objects.all()
    customer_count = customer.count()
    paginator = Paginator(customer, 5)
    page = request.GET.get('page')
    paged_customer = paginator.get_page(page)
    context = {
        'customer_count': customer_count,
        'customer': paged_customer,
        #'total_prix': total_prix,
    }
    return render(request, 'store/customer/customer.html', context)

@login_required(login_url='user-login')
def customer_detail(request, pk):
    single_customer = Customer.objects.get(id=pk)
    context = {
        'single_customer': single_customer
    }
    return render(request, 'store/customer/customer_detail.html', context)


@login_required(login_url='user-login')
def edit_customer(request, pk):
    item = Customer.objects.get(id=pk)
    if request.method == 'POST':
        form = customerForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil modifié avec succès !')
            return redirect('customer')
    else:
        form = customerForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'store/customer/edit_customer.html', context)


@login_required(login_url='user-login')
def customer_delete(request, pk):
    item = get_object_or_404(Customer, id=pk)
    item.delete()
    messages.success(request, 'Profil supprimé avec succès !')
    return redirect('customer')



#export data to excel

def export_data_product(request):
    products = Product.objects.all()
    data = []
    for product in products:
        msg = "Produits exportés avec succès, stocké dans le dossier produits"
        data.append({
               "nom":     product.product_name, 
                "Description":    product.description, 
                "Prix" : product.price, 
                "Stock Initial": product.stock_initial,
                "Stock Final" : product.stock, 
                "Vendus"        : product.sell, 
                "Ajouter"   : product.add_stock, 
                "Categorie"   : product.category,  
                "Fournisseur"   : product.supplier,  
                #"Date" : product.created_date, 
        }) 
    pd.DataFrame(data).to_excel('produits/produits.xlsx')
    messages.success(request, msg)
    return redirect('product')
