from unicodedata import category
from django.http import Http404
from django.shortcuts import render
from .models import Category, Image, Location
from django.core.exceptions import ObjectDoesNotExist

# Create your views here
def index(request):
  category = request.GET.get('category')
  if category == None:
     images = Image.objects.all()
  else:
    images = Image.objects.filter(category__name = category)

  categories = Category.objects.all()
  return render(request,'index.html',{'images':images, 'categories':categories})


def search_results(request):

    if 'category' in request.GET and request.GET['category']:
       search_term = request.GET.get('category')
       searched_images = Image.search_by_category(search_term)
       message = f"{search_term}"

       return render(request,'search.html',{"message":message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{'message':message})

def category_results(request,category):
  images = Image.filter_by_category(category)
  locations = Location.objects.all()
  categories = Category.objects.all()
  category = {'images':images,'locations':locations,'categories':categories}
  return render(request,'category.html',category)

def location(request, location_name):
  try:
    location = Location.objects.get(name =location_name)
  except ObjectDoesNotExist:
      raise Http404()
  return render(request,'location.html',{'location':location})