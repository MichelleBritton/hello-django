from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm



def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    # if it's a post request we'll get the information from the form that comes in from this template
    # and use it to create a new item and then redirect back to the todo list view
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form' : form
    }

    # If it's a get request we'll just return the add_item html template by rendering it
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    # Get a copy of the item from the database
    # This says that we want to get an instance of the item model with an ID equal to the item ID that was passed into the view via the URL 
    # This will either return the item if it exists or a 404 page if not.
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    # We'll create an instance of our item form and return it to the template in the context to pre-populate the form with the items current details
    form = ItemForm(instance=item)
    context = {
        'form' : form
    }

    return render(request, "todo/edit_item.html", context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')