from django.shortcuts import render,redirect
from .models import Post, BlogComment
from .templatetags import extras

# Create your views here.
def showBlogs(request):
    allPosts = Post.objects.all()
    # print(allPosts);
    # print(request.session["name"]);
    return render(request, "blogs/blogs.html", {"name": request.session["name"], "allPosts" : allPosts})


def blogpost(request,slug):
    # print(slug)
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    # print(replies)
    repDict={}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply) 
    # print(repDict)
    print(request.session["name"]);
    return render(request,"blogs/blogpost.html",{"name": request.session["name"],'post':post,'comments':comments, 'repDict':repDict})


def postComment(request):
    if request.method == 'POST':
        comment =  request.POST.get('comment')
        user = request.session["name"]
        postsno =request.POST.get('postsno')
        post = Post.objects.get(sno=postsno)
        parentsno = request.POST.get("parentsno")
        if parentsno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
        else:
            parent = BlogComment.objects.get(sno=parentsno)
            comment = BlogComment(comment=comment, user=user, post=post,parent=parent)
            comment.save()
        
    
    
    return redirect(f"/blogs/{post.slug}")