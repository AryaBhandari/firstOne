from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import signinForm,MyUserCreationForm
from django.contrib.auth import authenticate,login,logout
from staff.models import Staff
from student.models import Student,Education,Skill
from django.contrib.auth.decorators import login_required
from student.forms import StudentCreationForm,StudentEditForm
from .passwordGenerate import generatePassword
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import SignupRequest
# Create your views here.
@login_required(login_url='signin')
def Dashboard(request,id):
    if isStaff(id):
        return redirect('staffdash')
    if isStudent(id):
        return redirect('studentdash')

def signin(request):
    form = signinForm()
    if request.method == 'GET':
        return render(request, 'signin.html',{'form':form})
    else:
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if isStaff(user.id):
                return redirect('staffdash')
            if isStudent(user.id):
                return redirect('studentdash')
            return redirect('signout')
        else:
            messages.add_message(request, messages.ERROR, "Username or Password incorrect!")
            return render(request,'signin.html',{'form':form})



def signout(request):
    logout(request)
    return redirect('signin')

def signup(request):
    if request.method=='GET':
        form = StudentCreationForm()
        context = {
            'form':form,
        }
        return render(request,'signup.html',context)
    else:
        form = StudentCreationForm(request.POST, request.FILES)
        username = request.POST['Username']
        email = request.POST['email']

        fullname = request.POST['fullname']
        fathersname = request.POST['fathersname']
        mothersname = request.POST['mothersname']
        phoneno = request.POST['phoneno']
        parentsno = request.POST['parentsno']
        dob = request.POST['dob']
        permanentaddress = request.POST['permanentaddress']
        joindate = request.POST['joindate']
        idcard= request.FILES['idcard']
        profilepic=request.FILES['profile']
        if (len(str(phoneno))<10 or len(str(parentsno))<10):
            messages.add_message(request, messages.ERROR, "phone number should be at least 10 characters")
            return render(request,'signup.html',{'form':form})
        else:
            try:
                user = User(username=username, email=email)
                user.save()

                s = Student(fullname=fullname, fathersname=fathersname, mothersname=mothersname, phoneno=phoneno, idcard=idcard,profile=profilepic,
                            parentsno=parentsno, dob=dob, permanentaddress=permanentaddress,joindate=joindate,email=email, user=user)
                s.save()
                sr=SignupRequest(user=user)
                sr.save()
                messages.add_message(request, messages.SUCCESS, "Signed up successfully.. you will be notified via mail when your signup request has been accepted")
                return redirect('homepage')
            except:
                return render(request,'signup.html',{'form':form})


@login_required(login_url='signin')
def signupRequest(request):
    sr=SignupRequest.objects.all()
    context={
        'sr':sr,
    }
    return render(request,'signuprequest.html',context)

@login_required(login_url='signin')
def signupDetails(request, id):
    usr= User.objects.get(id=id)
    userrequest= SignupRequest.objects.get(user=usr)
    std=Student.objects.get(user=usr)
    form = StudentEditForm(request.POST or None, request.FILES or None, instance=std)
    if form.is_valid():

        try:
            password = generatePassword()
            userid = usr.id
            email = usr.email
            context = {
                'username': usr.username,
                'password': password,
                'userid': userid,
            }

            emailTemplate = get_template('emailtemplate.html').render(context)

            msg = EmailMessage(
                subject="Account Created",
                body=emailTemplate,
                from_email="hostelsanjivani@gmail.com",
                to=[email, ]
            )

            msg.content_subtype = 'html'
            msg.send()
            roomno = request.POST['roomno']
            std.roomno=roomno
            std.save()
            usr.set_password(password)
            usr.save()
            deleteSignupRequest(request,userrequest.id)
            messages.add_message(request, messages.SUCCESS, 'Student created successfully')
        except:
            messages.add_message(request,messages.ERROR,'sorry some error occured')
        return redirect('signuprequest')
    context = {
        'std': std,
        'form':form,
        'user':usr,
    }
    return render(request,'signupDetails.html',context)


@login_required(login_url='signin')
def studentList(request):
    std = Student.objects.all()
    context={
        'std':std,
    }
    return render(request,'studentlist.html',context)


@login_required(login_url='signin')
def studentDetail(request,id):
    std=Student.objects.get(id=id)
    context={
        'std':std,
        'educations': Education.objects.filter(student=std),
        'skills': Skill.objects.filter(student=std),
    }
    return render(request,'studentdetail.html',context)


@login_required(login_url='signin')
def deleteUser(request,id):
    user=User.objects.get(id=id)
    user.delete()
    messages.add_message(request,messages.SUCCESS,"User Deleted Successfully")
    return redirect('staffdash')

@login_required(login_url='signin')
def deleteSignupRequest(request,id):
    userRequest= SignupRequest.objects.get(id=id)
    userRequest.delete()
    messages.add_message(request,messages.SUCCESS,"success!")
    return redirect('signuprequest')


def isStaff(id):
    try:
        stf=Staff.objects.get(user_id=id)
        return True
    except:
        return False

def isStudent(id):
    try:
        stf=Student.objects.get(user_id=id)
        return True
    except:
        return False

@login_required(login_url='signin')
def currentlyLoginUser(request):
    student = Student.objects.get(user_id=request.user.id)
    return student