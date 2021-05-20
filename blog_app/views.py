from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blogpost,Content,Contact,Youtube,BlogComment,Contribute
from django.contrib import messages
from django.contrib.auth import authenticate, login as dlogin , logout
from django.contrib.auth.models import User
from blog_app.templatetags import extras
# overide original login
# Create your views here.

def index(request):
    objects = Blogpost.objects.all()
    params = {'objects':objects}
    return render (request,'index.html',params)


def result(request,myid):
    objects = Content.objects.filter(bp_id = myid)
    print(objects)
    yobjects = Youtube.objects.filter(bp_id = myid)
    bpobjects = Blogpost.objects.all()
    bpobject = Blogpost.objects.filter(post_id = myid).first()
    bpobject.views = bpobject.views + 1
    bpobject.save()
    allComments = BlogComment.objects.filter(post= myid,parent = None)
    replies = BlogComment.objects.filter(post= myid).exclude(parent = None)

    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno] = [reply].append(reply)
    
    params = {'objects':objects, 'bpobject':bpobject,'bpobjects':bpobjects,'yobjects':yobjects,'allComments':allComments, 'replyDict':replyDict} 
    return render (request,'result.html',params)

def basic(request,myid):
    objects = Blogpost.objects.all()
    params = {'objects':objects}
    return render (request,'basic.html',params)

def about(request):
    return render (request,'about.html')

def search(request):
    query= request.GET.get('search')
    if len(query) > 78:
       allPosts=Blogpost.objects.none()
    else:
        allPostsTitle= Blogpost.objects.filter(tilte__icontains=query)
        allPostsdesc= Blogpost.objects.filter(desc__icontains=query)
        
        allPosts=  allPostsTitle.union(allPostsdesc)
    if allPosts.count()==0:
        messages.warning(request, ("No search results found. Please refine your query."))
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'search.html', params)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        desc = request.POST.get('desc',"")
        contact = Contact( name = name, email = email, phone = phone, desc = desc)
        contact.save()
        done=True
        return render(request, 'contact.html', {'done':done})
    return render(request,"contact.html")


def handlesignup(request):
    if request.method =="POST":
        # Get the post parameters
        username = request.POST['name']
        email = request.POST['email']
        
        pass1 = request.POST['spassword1']
        pass2 = request.POST['spassword2']
        
        error = False
        # check for errorneous input
        if len(username)<10:
            error = True
            # messages.error(request, " Your username must be your full name")
            # return redirect('/')

        # if not username.isalnum():
        #     messages.error(request, " User name should only contain letters and numbers")
        #     return redirect('/')
        if pass1!= pass2:
            error = True
            #  messages.error(request, " Passwords do not match")
            #  return redirect('/')
        
        # if User.objects.filter(username=self.cleaned_data['username']).exists():
        # user = User.objects.get(username =username)
        # if len(user) > 0:
        #     error = True
            # messages.error(request, "Username already exist")
            # return redirect('/')
        
        if error == True:
            messages.error(request, "Invalid credentials")
            return redirect('/')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request,  "Your account created successfully")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")


def handlelogin(request): 
    if request.method =="POST":
        # Get the post parameters
        name = request.POST['lname']
        pass1 = request.POST['lpassword1']
        user = authenticate(username = name, password = pass1)
        
        if user is not None:
            dlogin(request, user)
            messages.success(request, "You are loggedin successfully")
            return redirect('/')
        else:         
            messages.error(request, "invalid credentials")
            return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')   

def postcomment(request):
    if request.method =="POST":
        comment=request.POST.get('comm')
        user = request.user
        postsno =request.POST.get('postsno')
        post= Blogpost.objects.get(post_id=postsno)
        parentsno= request.POST.get('parentsno')
        if parentsno == "":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentsno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
        
        return redirect(f"/result/{postsno}#com")   
    else:
        return HttpResponse("404 - Not found")

def contribute(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')

        contri = Contribute( name = name,desc = desc)
        contri.save()
        messages.success(request, "Thanks for your contribution! We will soon upload it on levelup")

    return render (request,'contribute.html')

       
     
     
       

    