from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from user.forms import CreateUserForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form = form.save()
            # group = Group.objects.get(name='Customers')
            # user.groups.add(group)
            messages.success(request, 'Vous êtes connecté avec succès !')
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)
# def profile(request):
#     context = {

#     }
#     return render(request, 'user/profile.html', context)