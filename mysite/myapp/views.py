from django.shortcuts import render
from .models import Food

def mv_list(request):
    foodss = Food.objects.all()
    return render(request,'myapp/mv_index.html',{'foodss':foodss})

def mv_list_2(request):
    food_list = Food.objects.all()
    return render(request,'myapp/mv_index_list.html',{'food_list':food_list})

def index(request):
    foods = Food.objects.all()
    return render(request,'myapp/index.html',{'foods':foods})