from django.shortcuts import redirect, render, get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from category.models import Category
from django.contrib import messages
from .forms import create_categoForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
@login_required(login_url='user-login')
def create_catego(request):
    if request.method == 'POST':
        form = create_categoForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.slug = slugify(category.category_name)
            category.save()
            messages.success(request, 'Catégorie crée avec succès !')
            return redirect('category_list')
    else:
        form = create_categoForm()
    context = {
        'form': form
    }
    return render(request, 'category/create_catego.html', context)

@login_required(login_url='user-login')
def category_list(request):
    category = Category.objects.all('-created_date')
    paginator = Paginator(category, 4)
    page = request.GET.get('page')
    paged_orders = paginator.get_page(page)
    context = {
        'category': paged_orders
    }
    return render(request, 'category/category_list.html', context)

@login_required(login_url='user-login')
def edit_catego(request, pk):
    item = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = create_categoForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Catégorie modifiée avec succès !')
            return redirect('category_list')
    else:
        form = create_categoForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'category/edit_catego.html', context)

@login_required(login_url='user-login')
def detail_catego(request, pk):
    single_catego = Category.objects.get(id=pk)
    context = {
        'single_catego': single_catego
    }
    return render(request, 'category/detail_catego.html', context)



@login_required(login_url='user-login')
def catego_delete(request, pk):
    item = get_object_or_404(Category, id=pk)
    item.delete()
    messages.success(request, 'Catégorie supprimée avec succès !')
    return redirect('category_list')