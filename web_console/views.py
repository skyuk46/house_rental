from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def uploadPost(request):
    return render(request,'upload_post.html')

def RoomPost(request):
	if request.method == 'POST': 
		form = RoomDetailsPostForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return HttpResponse('Successfully uploaded!') 
	else: 
	    form = RoomDetailsPostForm() 
	return render(request, 'roomPost.html', {'form' : form}) 
    
def userRegister(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else: 
	    form = UserRegisterForm() 
    return render(request, 'userRegister.html', {'form' : form})
