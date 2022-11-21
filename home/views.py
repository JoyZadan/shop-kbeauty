from django.shortcuts import render
from products.models import Brand

# Create your views here.


def index(request):
    """ A view to return the index page """
    brand = Brand.objects.all()[:8]
    context = {
        'brand': brand,
    }
    return render(request, 'home/index.html', context)
