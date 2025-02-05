from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import BookForm
from .models import Book,Giveaways

def home(request):
	count = User.objects.count()
	return render(request, 'home.html',{'count':count})

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserCreationForm
	return render(request,'registration/signup.html',{'form':form})

@login_required
def book_list(request):
	books = Book.objects.all()
	return render(request,'book_list.html',{'books':books})

def giveaways(request):
	items = Giveaways.objects.all()
	return render(request,'giveaways.html',{'items':items})

def upload_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			# messages.add_message(request,messages.SUCCESS,"You have uploaded successfully.")
			return redirect('book_list')
	else:
		form = BookForm()
	return render(request,'upload_book.html',{
		'form' : form
		})


def delete_book(request,pk): # pk = primary key
	if request.method == 'POST':
		book = Book.objects.get(pk=pk)
		book.delete()
	return redirect('book_list')
