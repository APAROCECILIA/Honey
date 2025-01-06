from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),

     path('about/', views.about, name='about'),
     path('chocolate/', views.chocolate, name='chocolate'),
     path('testimonial/', views.testimonial, name='testimonial'),
     path('contact/', views.contact, name='contact'),
]
