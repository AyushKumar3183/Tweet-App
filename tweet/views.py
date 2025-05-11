from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from .models import Tweet
from .forms import tweetform, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    return render(request,'index.html')

def tweetlist(request):
    tweets=Tweet.objects.all().order_by("-created")
    return render (request,"tweetlist.html",{'tweets':tweets})
@login_required
def tweetcreate(request):
    if request.method =="POST":
        form=tweetform(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect("tweetlist")
    else:
        form=tweetform()
    return render(request,'tweetform.html',{'form':form})    

@login_required
def tweetedit(request,tweetid):
    tweetobj=get_object_or_404(Tweet,pk=tweetid,user=request.user)
    if request.method =="POST":
        form=tweetform(request.POST,request.FILES,instance=tweetobj)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect("tweetlist")
    else:
        form=tweetform(instance=tweetobj)
    return render(request,'tweetform.html',{'form':form}) 


@login_required
def tweetdelete(request,tweetid):
     tweetobj=get_object_or_404(Tweet,pk=tweetid,user=request.user)
     if request.method =="POST":
        tweetobj.delete()
        return redirect("tweetlist")
     return render(request,'tweetdeleteform.html',{'tweetobj':tweetobj}) 

def register(request):
    if request.method =="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('login')
    else:
        form=UserRegistrationForm()    
    return render(request, 'registration/register.html', {'form': form})