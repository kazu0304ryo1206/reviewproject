from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from .models import ReviewModel
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

def signupview(request):
    #print('signup function is called')
    #print(request.POST.get('username_data'))
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        #user = User.objects.create_user(username_data,'',password)
        try:
            User.objects.create_user(username_data,'',password_data)
        except IntegrityError:
            return render(request,'signup.html',{'error':'このユーザーは既に登録されています。'})

        #username_data = request.POST['user_data']
        #password_data = request.POST['password_data']
        #user = User.objects.create_user(username_data,'',password_data)
        #print('POST method')
    else:
        print(User.objects.all())
        return render(request,'signup.html',{})
        #print(User.objects.all())
        #print('GET method probably...')
    return render(request,'signup.html',{})

    if request.method =='POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request,username=username_data,password=password_data)
        print(user)
        if user is None:
            login(request,user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request ,'login.html')

def loginview(request):
    if request.method =='POST':
        print('hellow!!')
        username_data = request.POST['username_data']
        print(username_data)
        password_data = request.POST['password_data']
        print(password_data)
        user = authenticate(request,username=username_data,password=password_data)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request,'login.html')

@login_required
def listview(request):
    print(User.objects.all())
    object_list = ReviewModel.objects.all()
    return render(request,'list.html',{'object_list':object_list})
    
@login_required    
def detailview(request,pk):
    object = ReviewModel.objects.get(pk=pk)
    return render(request,'detail.html',{'object':object})

class CreateClass(CreateView):
    template_name = 'create.html'
    mode = ReviewModel
    fields = ('tite','content','author','images','evaluation')
    success_url = reverse_lazy('list')

def logoutview(request):
    logout(request)
    return redirect('login')

def evaluationview(request,pk):
    post = ReviewModel.objects.get(pk=pk)
    author_name = request.user.get_username() +str(request.user.id)
    if author_name in post.useful_review_record:
        #return render(request,'detail.html',{'object':object})
        return redirect('list')
    else:
        post.useful_review = post.useful_review + 1
        post.useful_review_record = post.useful_review_record + author_name
        post.save()
        #return render(request,'detail.html',{'object':object})
        return redirect('list')


