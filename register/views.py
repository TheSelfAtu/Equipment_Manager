from django.contrib.auth import login
from django.shortcuts import render,redirect
from .models import User, Equipment
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.urls import reverse
from .forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

 

class EqDetail(DetailView):
    template_name = 'register/eq_detail.html'
    model = Equipment

class EqUpdate(UpdateView):
    template_name = 'register/equip_update.html'
    model = Equipment
    fields = ['name', 'category',  'price', 'comment']

    def get_success_url(self):
 
        return reverse('staff:equip_list')

class EqAdd(CreateView):
    template_name = 'register/equip_add.html'
    model = Equipment
    fields = ['name', 'category',  'price', 'comment']

    def get_success_url(self):
        return reverse('register:equip_add')

def SfAdd(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data['password']
            print(raw_password)
            user.set_password(raw_password)
            user.save()
            return redirect("staff:staff_page")
    else:
        form = UserCreationForm()
    return render(request, 'register/staff_add.html', {"form":form})