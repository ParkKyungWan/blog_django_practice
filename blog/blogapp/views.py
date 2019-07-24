from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Board
# Create your views here.
def home(request):
    posts = Board.objects.all
    return render(request,'home.html',{'posts':posts})

def detail(request,post_id):
    post = get_object_or_404(Board,pk=post_id) #pk는 primary_key
    return render(request,'detail.html',{'post':post})

def posting(request):
    return render(request,'posting.html')

def success(request):
    board = Board()
    board.title = request.GET['title']
    board.body = request.GET['body']
    board.image = request.GET['image']
    board.date = timezone.datetime.now()
    board.save()
    return redirect('/detail/'+str(board.id))