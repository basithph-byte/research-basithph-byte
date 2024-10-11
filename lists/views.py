from django.shortcuts import render, redirect, get_object_or_404
from .models import List, ListItem

# Create your views here.
def list_view(request):
    if request.method == 'POST':
        list_name = request.POST.get('list_name')
        new_list = List.objects.create(name=list_name)
        return redirect('list_detail', list_id=new_list.id)

    return render(request, 'lists/list_form.html')

def list_detail(request, list_id):
    list_obj = List.objects.get(id=list_id)
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        ListItem.objects.create(list=list_obj, item_name=item_name)

    items = list_obj.items.all()
    return render(request, 'lists/list_detail.html', {'list': list_obj, 'items': items})

def edit_item(request, list_id, item_id):
    list_obj = get_object_or_404(List, id=list_id)
    item = get_object_or_404(ListItem, id=item_id)

    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item.item_name = item_name
        item.save()
        return redirect('list_detail', list_id=list_id)

    return render(request, 'lists/edit_item.html', {'item': item, 'list': list_obj})

def delete_item(request, list_id, item_id):
    item = get_object_or_404(ListItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('list_detail', list_id=list_id)

    return render(request, 'lists/confirm_delete.html', {'item': item})