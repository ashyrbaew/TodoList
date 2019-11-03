from django.shortcuts import get_list_or_404, render, redirect
from django.http import HttpResponse
from .models import TodoList
from .forms import AddItemForm

def Index(request):
    ItemList = get_list_or_404(TodoList, visible=True)
    form = AddItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = AddItemForm()
        return redirect('/todo')
    content = {
        'form':form,
        'ItemList': ItemList
    }

    return render(request, 'todo/index.html', content)


def Visiblity(request, item_id):
    item = TodoList.objects.get( pk=item_id )
    item.visible = False
    item.save()
    response = redirect('/todo')
    return response