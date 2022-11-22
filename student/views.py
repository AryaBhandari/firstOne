from django.shortcuts import render,redirect
from .forms import StudentCreationForm,EducationCreationForm,SkillCreationForm,StudentEditForm,PaidForm
from .models import Student,Education,Skill,Fee
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from userauth.views import currentlyLoginUser
from django.contrib import messages
from userauth.views import isStudent,isStaff
# Create your views here.
@login_required(login_url='signin')
def dashboard(request):
    std = Student.objects.get(user=request.user)
    edu = EducationCreationForm(request.POST or None)
    s=SkillCreationForm(request.POST or None)
    if s.is_valid():
        skill=s.save(commit=False)
        skill.student=std
        skill.save()
        s=SkillCreationForm()
    if edu.is_valid():
        education = edu.save(commit=False)
        education.student=std
        education.save()
        edu=EducationCreationForm()
    context={
        'std':std,
        'skillform': s,
        'skills': Skill.objects.filter(student=std),
        'educationform': edu,
        'educations': Education.objects.filter(student=std),
    }
    return render(request,'student/dashboard.html',context)

@login_required(login_url='signin')
def removeSkill(request, id):
    skl= Skill.objects.get(pk=id)
    skl.delete()
    return redirect('studentdash')


@login_required(login_url='signin')
def removeEducation(request,id):
    edu= Education.objects.get(pk=id)
    edu.delete()
    return redirect('studentdash')


@login_required(login_url='signin')
def changePImage(request):
    if request.method=='POST':
        try:
            e = currentlyLoginUser(request)
            e.profile = request.FILES['image']
            e.save()
            messages.add_message(request,messages.SUCCESS,"successfully changed")
            return redirect('studentdash')
        except:
            messages.add_message(request, messages.ERROR, "couldn't change profile picture")
            return redirect('studentdash')

@login_required(login_url='signin')
def editProfile(request, id):
    p=Student.objects.get(id=id)
    form= StudentEditForm(request.POST or None,request.FILES or None, instance=p)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "profile updated successfully")
        if isStudent(request.user.id):
            return redirect('studentdash')
        if isStaff(request.user.id):
            return redirect('staffdash')
    return render(request,'student/editProfile.html',{'form':form})


@login_required(login_url='signin')
def editEducation(request,id):
    edu=Education.objects.get(id=id)
    form=EducationCreationForm(request.POST or None, instance=edu)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"successfully edited!")
        return redirect('studentdash')
    return render(request,'student/editEducation.html',{'form':form})


@login_required(login_url='signin')
def paidHistory(request,id):
    std = Student.objects.get(id=id)
    fee= Fee.objects.filter(student=std)
    if isStaff(request.user.id):
        form = PaidForm(request.POST or None)
        if form.is_valid():
            data=form.save(commit=False)
            data.student=std
            data.save()
            form = PaidForm()
        context = {
            'fee': fee,
            'std': std,
            'form':form,
        }
        return render(request,'staff/paidhistory.html', context)
    if isStudent(request.user.id):
        context = {
            'fee': fee,
            'std': std,
        }
        return render(request,'student/paidhistory.html',context)

