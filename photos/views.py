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
    if 'searchImage' in request.GET and request.GET['searchImage']:
        category = request.GET.get('searchImage')
        searched_images =Image.search_by_category(category)
        locations = Location.objects.all()
        categories = Category.objects.all()
        message = f'{category}'
        category_images = {'locations':locations, 'categories':categories, 'images':searched_images, 'message': message}
        return render(request, 'search.html', category_images)
    else:
        message = 'Enter category to search'
        return render(request, 'search.html', {'message':message})

def category_results(request,category):
  images = Image.filter_by_category(category)
  locations = Location.objects.all()
  categories = Category.objects.all()
  category = {'images':images,'locations':locations,'categories':categories}
  return render(request,'category.html',category)

def location_results(request,location):
    images = Image.filter_by_location(location)
    locations = Location.objects.all()
    categories = Category.objects.all()
    location = {'images':images,'locations':locations, 'categories':categories }
   

    return render(request, 'location.html',location)