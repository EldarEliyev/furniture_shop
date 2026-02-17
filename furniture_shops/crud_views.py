from django.shortcuts import render, redirect, get_object_or_404
from.models import Furniture
from.forms import FurnitureForm

def home(request):
    return render(request, "furniture_shops/home.html")

def furniture_list(request):
    furnitures = Furniture.objects.all().order_by('-created_at').filter(is_available=True)
    return render(request,  "furniture_shops/furniture_list.html",  {"furnitures": furnitures})

def add_furniture(request):
    if request.method == "POST":
        form = FurnitureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("furniture_list")
    else:
        form = FurnitureForm()
    return render(request,  "furniture_shops/add_furniture.html",  {"form": form})

def furniture_detail(request,  furniture_id):
    furniture = Furniture.objects.get(id=furniture_id)
    return render(request, "furniture_shops/furniture_detail.html",  {"furniture": furniture})


def update_furniture(request,  furniture_id):
    furniture = get_object_or_404(Furniture, id=furniture_id)
    if request.method == "POST":
        form = FurnitureForm(request.POST, request.FILES, instance=furniture)
        if form.is_valid():
            form.save()
            return redirect("furniture_list")
    else:
        form = FurnitureForm(instance=furniture)
    return render(request, "furniture_shops/update_furniture.html",  {"form": form, "furniture": furniture})


def delete_furniture(request, furniture_id):
    furniture = get_object_or_404(Furniture, id=furniture_id)
    if request.method == "POST":
        furniture.delete()
        return redirect("furniture_list")
    return render(request,  "furniture_shops/delete_furniture.html",  {"furniture": furniture})

