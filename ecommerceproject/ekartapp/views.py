from pickle import GET

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category,Product
# Create your views here.
from  django.core.paginator import Paginator,EmptyPage,InvalidPage
def index(request):
    return HttpResponse("hy")
def allProdcat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!= None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)

    return render(request,"category.html",{'category':c_page,'products':products})
def proDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Product.DoesNotExist:
        # Handle the case where the product is not found
        return render(request, 'product_not_found.html')  # You can create a template for this case
    except Exception as e:
        # Log or handle other exceptions
        raise e

    return render(request, 'product.html', {'product': product})
