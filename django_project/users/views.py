from django.shortcuts import render,redirect
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You have been successfully registered')
            return redirect('blog-home')

    else:
        form=UserRegisterForm()

        
    return render(request,'users/register.html',{'form':form})
 #Yet to be developed   
'''@login_required
def profile(request):
    return render(request,'users/profile.html')'''