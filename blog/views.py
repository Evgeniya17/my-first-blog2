from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from . import urls
from .forms import PostForm
from django.shortcuts import redirect

from django.http import HttpResponseRedirect
from .forms import NameForm
from .models import Name


from .models import Comment 
from .forms import CommentForm


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})



def get_name(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    else:
        form = NameForm()
        names = Name.objects.all()
    return render(request, 'name.html', {'form': form, 'names': names})


def post_detail(request, pk):  
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)  
    new_comment = None  
    if request.method == 'POST':  
        comment_form = CommentForm(data=request.POST)  
        if comment_form.is_valid():  
          new_comment = comment_form.save(commit=False)  
          new_comment.post = post  
          new_comment.save()  
    else:  
        comment_form = CommentForm()  
    return render(request,    'blog/post_detail.html',  
		  {'post': post,  
		  'comments': comments,  
		  'new_comment': new_comment,  
		  'comment_form': comment_form})
    






