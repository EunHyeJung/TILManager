from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    # result_list = list(get_object_or_404(Post, pk=pk))
    post = Post.objects.filter(pk=pk)
    return HttpResponse(serializers.serialize("json", post), content_type="application/json")
