from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Til, Review, Plan, Post
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def til_list(request):
    posts = Post.objects.all()
    return render(request, 'til/til_list.html', {
        'posts': posts
    })




def til_detail(request, pk):
    response_data = {}
    post = Post.objects.filter(pk=pk)
    response_data['post'] = serializers.serialize("json", post)
    tils = Til.objects.filter(post__pk=pk)
    response_data['tils'] = serializers.serialize("json", tils)
    reviews = Review.objects.filter(post__pk=pk)
    response_data['reviews'] = serializers.serialize("json", reviews)
    plans = Plan.objects.filter(post__pk=pk)
    response_data['plans'] = serializers.serialize("json", plans)

    # return HttpResponse(serializers.serialize("json", resultset), content_type="application/json")
    return HttpResponse(json.dumps(response_data, ensure_ascii=False), content_type="application/json;charset=utf-8")
