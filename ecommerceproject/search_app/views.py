from django.shortcuts import render
from ekartapp.models import Product
from django.db.models import Q

# Create your views here.
def SearchResult(request):
    products = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.filter(Q(name__contains=query) | Q(description__contains=query))
        print(f"Search Query: {query}")
        print(f"Search Results: {products}")

    return render(request, 'search.html', {'query': query, 'products': products})
