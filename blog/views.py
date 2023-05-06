from django.shortcuts import  render
from .models import Post
from django.shortcuts import get_object_or_404

def render_posts(request):
    posts = Post.objects.all()

    return render (request,'posts.html',{
        'posts':posts
    })

def post_detail(request, post_id):
    
    detail=get_object_or_404(Post,pk=post_id) #obtiene 1 objeto, no ocupas for
    #detail=Post.objects.filter(id=post_id) #obtiene lista de objetos y ocupas un for
    
    return render(request, 'post_detail.html',{
        'detail':detail
        
    })
