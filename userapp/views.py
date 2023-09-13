from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from .forms import signup_form,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
def userview(request):
    if request.method=='POST':
        form=signup_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form=signup_form()
    return render(request,'signup.html',{'form':form})
@login_required
def profile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST or None,instance=request.user)
        p_form=ProfileUpdateForm(request.POST or None,request.FILES,instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    u_form=UserUpdateForm(instance=request.user)
    p_form=ProfileUpdateForm(instance=request.user.profilemodel)
    return render(request,'profile.html',{'u_form':u_form,'p_form':p_form})
