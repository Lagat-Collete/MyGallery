from django.conf.urls import url 
from . import views
from django.urls import path


urlpatterns=[
    path('',views.photos, name= 'indexPhotos'),
    path('search/', views.search_results, name='search_results')
]