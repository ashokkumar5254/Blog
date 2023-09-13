from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PostModel
from .forms import post_form,comment_form
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    data=PostModel.objects.all()
    if request.method=='POST':
        form=post_form(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('index')
    else:
        form=post_form()
    return render(request,'index.html',{'data':data,'form':form})
@login_required
def detail_page(request,pk):
    data=PostModel.objects.get(id=pk)
    if request.method=='POST':
        form=comment_form(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.post=data
            instance.save()
            return redirect('detail_page',pk=data.id)
    else:
        form=comment_form()
    return render(request,'detail.html',{'data':data,'form':form})

def detail_editpage(request,pk):
    data=PostModel.objects.get(id=pk)
    if request.method=='POST':
        form=post_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('detail_page',pk=data.id)
    else:
        form=post_form(instance=data)
        return render(request,'detail_editpage.html',{'form':form})
def delete_view(request,pk):
    data=PostModel.objects.get(id=pk)
    if request.method=='POST':
        data.delete()
        return redirect('index')
    return render(request,'delete.html')

# Create your views here.
