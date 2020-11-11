from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    bestRoom_raw = RoomDetails.objects.filter(balcony= 1)
    if (len(bestRoom_raw) > 4):
        bestRoom = bestRoom_raw[0:4]
        print('0')
    else:
        bestRoom = bestRoom_raw

    context = {
        'bestRoom' : bestRoom,
    }
    return render(request, 'index.html',context)

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

def roomDetails(request):
    if request.method == 'GET':
        id = int(request.GET.get('roomDetails'))
        room = RoomDetails.objects.get(id = id)
        context = {
            'room' : room,
        }
        return render(request, 'room-detail.html',context)

def roomList(request):
    roomList = RoomDetails.objects.all()
    context = {
        'roomList' : roomList
    }
    return render(request,'room-list.html',context)