from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage

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
def secret_page(request):
	return render(request, 'secret_page.html')

class SecretPage(LoginRequiredMixin, TemplateView):
	template_name = 'secret_page.html'

def upload(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		context['url'] = fs.url(name)
	return render(request, 'upload.html',context)