from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Reply
from .forms import PostForm, ReplyForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'discussion/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'discussion/post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'discussion/create_post.html', {'form': form})

def create_reply(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = ReplyForm()
    return render(request, 'discussion/create_reply.html', {'form': form, 'post': post})
