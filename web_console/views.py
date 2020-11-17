from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

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

def RoomPost(request):
	if request.method == 'POST':
		form = RoomDetailsPostForm(request.POST, request.FILES) 
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/RoomPost',{'response': 'Đăng bài thành công !'}) 
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
        ownerId = room.owner_id
        owner = Users.objects.get(user_id = ownerId)
        context = {
            'room' : room,
            'owner' : owner
        }
        return render(request, 'room-detail.html',context)

def roomList(request):
    roomList = RoomDetails.objects.all()
    context = {
        'roomList' : roomList
    }
    return render(request,'room-list.html',context)

def search(request):
    Keyword = request.GET.get("Keyword")
    roomType = request.GET.get('roomType')
    district = request.GET.get('district')
    area = int(request.GET.get('area'))
    bedrooms = int(request.GET.get('bedrooms'))
    bathrooms = int(request.GET.get('bathrooms'))
    kitchens = int(request.GET.get('kitchens'))
    searchResult_raw1 = RoomDetails.objects.filter(roomAddress__icontains = Keyword)
    if (roomType == "All"):
        searchResult_raw2 = searchResult_raw1.all()
    else:
        searchResult_raw2 = searchResult_raw1.filter(roomType_icontains = roomType)
    if (roomType == "All"):
        searchResult_raw3 = searchResult_raw2.all()
    else:
        searchResult_raw3 = searchResult_raw2.filter(roomAddress__icontains = district)

    searchResult = searchResult_raw3.filter(area__lt = area, bedroom__lt = bedrooms, bathroom__lt = bathrooms, kitchen__lt = kitchens)
    lenSearchResult = len(searchResult)
    context = {
        'searchResult' : searchResult,
        'lenSearchResult' : lenSearchResult
    }
    return render(request,'searchResult.html',context)

def ownerRoomList(request):
    # ownerId = request.GET.get('ownerId')
    ownerId = 1
    roomList = RoomDetails.objects.filter(owner_id=ownerId)
    context = {
        'roomList' : roomList
    }
    return render(request,'owner-room-list.html',context)