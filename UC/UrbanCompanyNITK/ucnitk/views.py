from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'ucnitk/customer.html')

class customer(View):
    def get(self, request):
        services =  Service.objects.all()
        servicelist = {}
        servicetable = {}
        
        i = 1
        for service in services:
            servicelist.add(service.ServiceName)
            if i%3==0:
                servicetable.add(servicelist)
                servicelist.clear()  
            i+=1      
        return render(request, 'ucnitk/customer.html', {'servicetable':servicetable})


def add_something(request):
    return render(request, 'ucnitk/add_something.html')

def order_service(request):
    return render(request, 'ucnitk/order_service.html')

class service_provider(View):
    def get(self, request):
        user = request.user
        context = {
            'orders': Order.objects.exclude(Customer = user).filter(ServiceProvider = None)
        }
        return render(request, 'ucnitk/service_provider.html', context)

# @login_required(login_url='/login/')
class your_orders(View):
    def get(self, request):
        user = request.user
        context = {
            'orders': Order.objects.filter(Customer = user)
        }
        return render(request, 'ucnitk/your_orders.html', context)

# @login_required(login_url='/login/')
class accepted_orders(View):
    def get(self, request):
        user = request.user
        context = {
            'orders': Order.objects.filter(ServiceProvider = user)
        }
        return render(request, 'ucnitk/accepted_orders.html', context)

class OrderDetailView(DetailView):
    model = Order
