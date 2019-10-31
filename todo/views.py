from django.shortcuts import get_list_or_404, render
from .models import TodoList

def TodoIndex(request):
    ItemList = get_list_or_404( TodoList, status=0 )
    return render(request, 'todo/index.html', {'ItemList': ItemList})


def ChangeStatus(request, item_id):
    item = TodoList.objects.get( pk=item_id )
    item.status = 1
    item.save()