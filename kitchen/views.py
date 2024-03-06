from django.shortcuts import render,redirect,get_object_or_404
from .models import FoodMenu
from .forms import MenuForm, UpdateMenuForm
from django.contrib import messages

def food_menu(request):
    food_item = FoodMenu.objects.all().order_by('-date_added')
    context = {
        "food_item": food_item,
    }

    return render(request, "kitchen/food_menu.html", context)

def menu(request):
    food = FoodMenu.objects.all().order_by('-date_added')
    context = {
        "food": food,
    }

    return render(request, "kitchen/menu.html", context)

def add_food_item(request):
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            image = form.cleaned_data.get('image')

            FoodMenu.objects.create(name=name, price=price, image=image)
            return redirect('menu_preview')
        else:
            error_message = "sorry something went wrong"
    else:
        form = MenuForm()

    context = {
        "form": form,
    }

    return render(request, "kitchen/add_food_item.html", context)

def item_detail(request, pk):
    food_item = get_object_or_404(FoodMenu, pk=pk)
    context = {
        "food_item": food_item,
    }

    return render(request, "kitchen/food_detail.html", context)
def update_menu(request, pk):
    food_item = get_object_or_404(FoodMenu, pk=pk)

    if request.method == "POST":
        form = UpdateMenuForm(request.POST, request.FILES, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('menu_preview')
    else:
        form = UpdateMenuForm(instance=food_item)

    context = {
        "food_item": food_item,
        "form": form,
    }

    return render(request, "kitchen/update_menu.html", context)