from django.shortcuts import get_object_or_404, redirect, render
from crudapp.models import Item

# Create your views here.

# Model to create item in the database 
def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Item.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request, 'item_form.html')


# Reading items from the database
def read_item(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})


# Updating an item
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')  # Fixed the typo here
        item.save()
        return redirect('item_list')
    return render(request, 'item_form.html', {'item': item})


# Deleting an item from the database
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})
