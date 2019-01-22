from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import student
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import studentreg , userform
from .models import studentsignup



def log_out(request):
    logout(request)
    return redirect(('home'))
def log_in(request):

        if request.method=="POST":
            print(request.POST)
            u=request.POST.get("username")
            p=request.POST.get("password")
            user=authenticate(request,username=u,password=p)
            if user is not None:
                login(request,user)
                messages.success(request, ' Welcome to Tech Fest '+ u )
                return redirect("home")
        return render(request,'accounts/login.html')


"""def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            s=student(username=username,password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})"""

def studentform(request):

    if request.method == 'POST':
        form = studentreg(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request,'you details submiited ')
            return HttpResponseRedirect('')
    else:
        form = studentreg()

    return render(request,'accounts/studentform.html',{'form':form})


def sign_up(request):
    if request.method == 'POST':
        form1 = userform(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['email']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password=form1.cleaned_data['password']
            User.objects.create_user(username=username,first_name=first_name,last_name =last_name,email=email,password =password)
            return HttpResponseRedirect('')

    else:
        form1 = userform()
    return render(request,'accounts/register.html',{'form':form1})


