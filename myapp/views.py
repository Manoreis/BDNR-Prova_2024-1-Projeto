from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Car

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cars')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarCreateView(CreateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['marca', 'modelo', 'ano']
    success_url = reverse_lazy('car-list')

class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['marca', 'modelo', 'ano']
    success_url = reverse_lazy('car-list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = reverse_lazy('car-list')

def car_list_json(request):
    cars = Car.objects.all().values('marca', 'modelo', 'ano')
    return JsonResponse(list(cars), safe=False)
