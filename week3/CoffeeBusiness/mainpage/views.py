from django.contrib.auth.models import User
from django.shortcuts import render

from product.models import Product


def landing(request):
    user = None
    if request.session.get('id'):
        user = User.objects.get(id=request.session.get('id'))

    context = {
        'user': user
    }
    return render(request, "index.html", context=context)

def about(request):
    user = None
    if request.session.get('id'):
        user = User.objects.get(id=request.session.get('id'))

    context = {
        'user': user
    }
    return render(request, "about.html", context=context)

def products(request):
    user = None
    contents = Product.objects.all()
    content_list1 = contents[0] #Product.objects.get(id=2)
    content_list2 = contents[1]
    content_list3 = contents[2]
    if request.session.get('id'):
        user = User.objects.get(id=request.session.get('id'))

    context = {
        'user': user,
        'content_list1' : content_list1,
        'content_list2' : content_list2,
        'content_list3' : content_list3,
    }
    return render(request, "products.html", context=context)