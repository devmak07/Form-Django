from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import formdata
from .models import form_detail
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details:loginPage')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('details:read_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login_register.html', {'form': form})

def create_form_detail(request):
    if request.method == "POST":
        form = formdata(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        if request.user.is_authenticated:
            return redirect('details:read_list')
        else:
            return redirect('details:register_view')
    else:
        form = formdata()
    return render(request, 'index.html', {'form': form})



@login_required(login_url='details:loginPage')
def read_list(request):
    query = request.GET.get('q')  # Corrected: 'GET' should be in all uppercase
    if query:
        # Filter the form_details based on the query
        form_details = form_detail.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(address__icontains=query)
        )
    else:
        # If no query is provided, return all form_details
        form_details = form_detail.objects.all()

    return render(request, 'index2.html', {'form_details': form_details, 'query': query})


@login_required(login_url='details:loginPage')
def update_form_detail(request, pk):
    form_detail_instance = get_object_or_404(form_detail, pk=pk)
    if request.method == "POST":
        form = formdata(request.POST, instance=form_detail_instance)
        if form.is_valid():
            form.save()
        return redirect('details:read_list')
    else:
        form = formdata(instance=form_detail_instance)
    return render(request, 'index.html', {'form': form})

@login_required(login_url='details:loginPage')
def delete(request, pk):
    form_detail_instance = get_object_or_404(form_detail, pk=pk)
    form_detail_instance.delete()
    return redirect('details:read_list')

def logout_view(request):
    auth_logout(request)
    return redirect('details:loginPage')
