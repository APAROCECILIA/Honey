from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),

     path('about/', views.about, name='about'),
     path('honey/', views.honey, name='honey'),
     path('testimonial/', views.testimonial, name='testimonial'),
     path('contact/', views.contact, name='contact'),
     path('footer/', views.footer, name='footer'),
]
