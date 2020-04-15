from django.shortcuts import get_list_or_404, render, redirect
from django.http import HttpResponse
from .models import TodoList
from .forms import AddItemForm

from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 

def Index(request):
    if request.user.is_authenticated:
        ItemList = get_list_or_404(TodoList)
        form = AddItemForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = AddItemForm()
            return redirect('/todo')
        content = {
            'ItemList': ItemList,
            'form':form,
        }
        return render(request, 'todo/index.html', content)
    else:
        return redirect('/login')

def Visiblity(request, item_id):
    if request.user.is_authenticated:
        item = TodoList.objects.get( pk=item_id )
        if item.visible == False:
            item.visible = True
            item.save()
            return redirect('/todo')
        else:
            item.visible = False
            item.save()
            return redirect('/todo')
    else:
        return redirect('/login')
        
