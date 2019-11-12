from django.shortcuts import get_list_or_404, render, redirect
from django.http import HttpResponse
from .models import TodoList
from .forms import AddItemForm

def Index(request):
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


# def addnew(request):
#     form = AddItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = AddItemForm()
#         return redirect('/todo')
#     content = {
#         'form':form,
#     }
#     return render(request, 'todo/form.html', content)


def Visiblity(request, item_id):
    item = TodoList.objects.get( pk=item_id )
    if item.visible == False:
        item.visible = True
        item.save()
        return redirect('/todo')
    else:
        item.visible = False
        item.save()
        return redirect('/todo')