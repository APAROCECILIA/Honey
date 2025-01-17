from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def honey(request):
    return render(request, 'honey.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def contact(request):
    return render(request, 'contact.html')

def footer(request):
    return render(request, 'footer.html')

