# from django.core import serializers
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.utils import timezone
#
# from .forms import PostForm
# from .models import Post
#
#
# # Create your views here.
# def index(request):
#     return render(request, 'home/index.html',)
#
# def post_list(request):
#     posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})
#
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.created_date = timezone.now()
#             post.save()
#         return redirect('post_list')
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
#
#
# def post_detail(request, pk):
#     # result_list = list(get_object_or_404(Post, pk=pk))
#     post = Post.objects.filter(pk=pk)
#     return HttpResponse(serializers.serialize("json", post), content_type="application/json")
