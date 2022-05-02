from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from product.forms import CommentForm
from product.models import Product, Comment


# Create your views here.

def detail(request, content_id):
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

@login_required(login_url='accounts:login')
def comment_create(request, content_id):
    user = None
    if request.session.get('id'):
        user = User.objects.get(id=request.session.get('id'))

    content = get_object_or_404(Product, pk=content_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = content
            comment.author = user
            comment.save()
            return redirect('detail', content_id=content.id)
    else:
        form = CommentForm()
        context = {'content': content, 'form': form}
        return render(request, 'productdetail.html', context)

@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    user = None
    if request.session.get('id'):
        user = User.objects.get(id=request.session.get('id'))

    comment = get_object_or_404(Comment, pk=comment_id)
    if user != comment.author:
        raise PermissionDenied
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)
        context = {'comment': comment, 'form': form}
        return render(request, 'comment_form.html', context)

@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    user = None
    if request.session.get('id'):
        user = User.objects.get(id=request.session.get('id'))

    comment = get_object_or_404(Comment, pk=comment_id)
    if user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
        return redirect('detail', content_id=comment.content_list.id)