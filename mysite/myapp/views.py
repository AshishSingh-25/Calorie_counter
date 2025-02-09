from django.shortcuts import render,redirect
from .models import Food,Consume

def index(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)    
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})

def delete_consume(request,id):
    consume_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consume_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')

#Practice templates

def mv_list(request):
    foodss = Food.objects.all()
    return render(request,'myapp/mv_index.html',{'foodss':foodss})

def mv_list_2(request):
    food_list = Food.objects.all()
    return render(request,'myapp/mv_index_list.html',{'food_list':food_list})