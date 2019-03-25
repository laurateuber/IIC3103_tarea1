from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('films/<int:url_id>/', views.movie, name='movie'),
    path('people/<int:url_id>/', views.people, name='people'),
    path('planets/<int:url_id>/', views.planet, name='planet'),
    path('starships/<int:url_id>/', views.starship, name='starship'),
    path('search/', views.search, name='search')
    ]
