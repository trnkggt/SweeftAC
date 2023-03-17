from django.urls import path

from . import views

urlpatterns = [

    path('shorten/', views.urlshortener),
    path('<shorturl>/', views.urlviewer),

]