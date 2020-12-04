from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import datetime

def index(request):
    bestRoom_raw = RoomDetails.objects.filter(balcony= 1)
    if (len(bestRoom_raw) > 4):
        bestRoom = bestRoom_raw[0:4]
        print('0')
    else:
        bestRoom = bestRoom_raw

    waitingUser = WaitingList.objects.all()
    waitingCount = len(waitingUser)
    context = {
        'bestRoom' : bestRoom,
        'waitingCount' : waitingCount
    }
    return render(request, 'index.html',context)

def about(request):
    waitingUser = WaitingList.objects.all()
    waitingCount = len(waitingUser)
    return render(request, 'about.html',{'waitingCount' : waitingCount})

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
        confirmed = 0
        if (form.data['user_type'] == "renter"):
            confirmed = 1
        if form.is_valid() and confirmed == 1:
            form.save()
            return HttpResponseRedirect('/')
        else:
            waitingUser = WaitingList(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'], name = form.cleaned_data['name'], birth = form.cleaned_data['birth'], phone = form.cleaned_data['phone'], address = form.cleaned_data['address'], user_type = form.cleaned_data['user_type'])
            waitingUser.save()
            return render(request,'userRegister.html',{'message': "Tài khoản của bạn đang được xét duyệt"})
    else: 
	    form = UserRegisterForm() 
    return render(request, 'userRegister.html', {'form' : form})

def roomDetails(request):
    if request.method == 'GET':
        id = int(request.GET.get('roomDetails'))
        room = RoomDetails.objects.get(id = id)
        ownerId = room.owner_id
        owner = Users.objects.get(user_id = ownerId)
        waitingUser = WaitingList.objects.all()
        waitingCount = len(waitingUser)

        comments = Comment.objects.filter(room_id= id)
        numberOfComment = len(comments)

        rates = Rating.objects.filter(room_id= id)

        context = {
            'room' : room,
            'owner' : owner,
            'waitingCount' : waitingCount,
            'comments' : comments,
            'numberOfComment' : numberOfComment,
            'rates' : rates
        }
        return render(request, 'room-detail.html',context)

def roomList(request):
    roomList = RoomDetails.objects.all()
    waitingUser = WaitingList.objects.all()
    waitingCount = len(waitingUser)
    context = {
        'roomList' : roomList,
        'waitingCount' : waitingCount
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
    waitingUser = WaitingList.objects.all()
    waitingCount = len(waitingUser)
    context = {
        'searchResult' : searchResult,
        'lenSearchResult' : lenSearchResult,
        'waitingCount' : waitingCount
    }
    return render(request,'searchResult.html',context)

def ownerRoomList(request):
    ownerId = request.GET.get('ownerId')
    roomList = RoomDetails.objects.filter(owner_id=ownerId)
    waitingUser = WaitingList.objects.all()
    waitingCount = len(waitingUser)
    context = {
        'roomList' : roomList,
        'waitingCount' : waitingCount
    }
    return render(request,'owner-room-list.html',context)

def userConfirm(request):
    if (request.method == "GET"):
        decision = request.GET.get('decision')
        username = request.GET.get('username')
        if (username):
            user = WaitingList.objects.get(username=username)
            if (decision == 'accept'):
                email = user.email
                password = user.password
                name = user.name
                birth = user.birth
                phone = user.phone
                address = user.address
                Users.objects.create_user(username=username, email=email,password = password, name = name, birth = birth, phone = phone, address = address, user_type = "owner")
                WaitingList.objects.get(username= username).delete()
                return HttpResponseRedirect('/userConfirm')
            elif (decision == 'decline'):
                WaitingList.objects.get(username= username).delete()
                return HttpResponseRedirect('/userConfirm')
            
    waitingList = WaitingList.objects.all()
    context = {
        'waitingList' : waitingList
    }
    return render(request,'user-confirm.html',context)

def postComment(request):
    if(request.method == "GET"):
        author = request.GET.get('author')
        body = request.GET.get('body')
        date = datetime.datetime.now()
        room_id = int(request.GET.get('room'))
        comment = Comment(room_id = room_id, author = author, body = body,date = date)
        comment.save()
        return HttpResponse('Bình luận thành công!')

def userProfile(request):
    return render(request,'userProfile.html')

def update_rating(request):
    message = ""
    if request.method == 'POST':
        id = int(request.POST.get('room_id'))
        rate = int(request.POST.get('rating'))
        rater = request.POST.get('rater')
        rating = ""

        for i in range(1,rate + 1):
            rating = rating + str(i)
        
        newRating = Rating(room_id= id, rating= rating,rater= rater)
        newRating.save()
        message = 'update successful'
    return HttpResponse(message)

