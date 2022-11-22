from django.shortcuts import render,redirect
from .forms import StaffCreationForm
from .models import Staff
from student.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from userauth.models import SignupRequest
# Create your views here.

@login_required(login_url='signin')
def changeStaffImage(request):
    if request.method=='POST':
        try:
            e = currentlyLoginStaff(request)
            print("----------------------------")
            e.profile = request.FILES['image']
            e.save()
            messages.add_message(request,messages.SUCCESS,"successfully changed")
            return redirect('staffdash')
        except:
            messages.add_message(request, messages.ERROR, "couldn't change profile picture")
            return redirect('staffdash')

@login_required(login_url='signin')
def dashboard(request):
    stf= Staff.objects.get(user=request.user)
    std= Student.objects.all()
    context={
        'stf':stf,
        'std':std
    }
    return render(request,'staff/staffdash.html',context)

@login_required(login_url='signin')
def editProfile(request,id):
    p= Staff.objects.get(id=id)
    form = StaffCreationForm(request.POST or None,request.FILES or None,instance=p)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"Profile Updated Successfully")
        return redirect('staffdash')
    return render(request,"staff/editStaffProfile.html",{'form':form})

@login_required(login_url='signin')
def currentlyLoginStaff(request):
    staff = Staff.objects.get(user_id=request.user.id)
    return staff