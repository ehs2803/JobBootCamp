from django.contrib.auth.models import User
from django.shortcuts import render
from product.models import Product
# Create your views here.

def detail(request, content_id):
    print(content_id)
    user = None
    content = Product.objects.get(id=content_id)
    if request.session.get('id'):
        user = User.objects.get(id=request.session.get('id'))

    context = {
        'user': user,
        'pid' : content_id,
        'content' : content,
    }
    return render(request, "productdetail.html", context=context)
