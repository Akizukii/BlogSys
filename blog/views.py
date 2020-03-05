from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Post, Category, Comment

# Create your views here.

def custom_proc(request):
    # 上下文处理器
    categories = Category.objects.all()
    return {
        "categories":categories,
    }

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts':posts})

@require_http_methods(["GET", "POST"])
def post(request, post_id, reply=None):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('text'))
        name = request.POST.get('name')
        text = request.POST.get('text')
        comment = Comment(author=name, text=text, post=post)
        if request.session.get('reply'):
            print('get reply')
            comment.replied = get_object_or_404(Comment, id=request.session.get('reply'))
            request.session['reply'] = None
        comment.save()
        return redirect('/blog/post/{}'.format(post.id))


    comments = post.comment_set.all()
    context={
        'post': post,
        'comments': comments,
    }
    return render(request, 'post.html', context=context)

def reply_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    request.session['reply'] =  comment_id
    return redirect('/blog/post/{}#comment-form'.format(comment.post.id))

def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    posts = category.post_set.all()
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'category.html', context=context)

def tt(request):
    return render(request, 'base.html')