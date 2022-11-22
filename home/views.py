from django.shortcuts import render
from products.models import Brand

# Create your views here.


def index(request):
    """ A view to return the index page """
    brands = Brand.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, 'home/index.html', context)
