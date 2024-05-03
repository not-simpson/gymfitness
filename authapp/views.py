from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from authapp.models import Contact,MembershipPlan,Trainer,Enrollment
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def Home(request):
    return render(request,"index.html")
def gallery(request):
    return render(request,"gallery.html")

def signup(request):
    if request.method=="POST":
        email=request.POST.get('email')
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1 != pass2:
            messages.info(request,"Passwords are not matching")
            return redirect('/signup') 

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is taken")
                return redirect('/signup')
        
        except Exception as identifier:
            pass

        try:
            if User.objects.get(username=username):
                messages.warning(request,"Username is taken!!!")
                return redirect('/signup')

        except Exception as identifier:
            pass

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        return redirect('/login')  

    return render (request,"signup.html")

def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,'invalid details')
            return redirect('/login')

    return render(request,"handlelogin.html")


def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect('/login')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()
        
        messages.info(request,"Thanks for contacting us, we'll get back to you soon")
        return redirect('/contact')
    
    return render(request,"contact.html")

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and try again")
        return redirect("/login")
    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        address=request.POST.get('address')
        query=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipplan=member,SelectTrainer=trainer,Address=address)
        query.save()
        messages.success(request,"Thanks for enrolling")
        return redirect("/join")
        
    return render(request,"enroll.html",context)


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and try again")
        return redirect("/login")
    user_name=request.user
    posts=Enrollment.objects.filter(FullName=user_name)
    print(posts)
    context={"posts":posts}
    return render(request,"profile.html",context)