from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from init.forms import CamForm, VideoGrapherRegisterForm, VideoGrapherProfile,UserRegistForm,CustomerProfile,PasswordChange,OrderForm, viewCustOrderForm
from django.contrib.auth.decorators import login_required
from init.models import OrderModel, User,CamModels
from django.contrib.auth import authenticate, login
from MyVideoGrapher import settings
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    videog = User.objects.filter(hadFilled = 1)
    c = videog.count()
    cam = CamModels.objects.filter(vgId = request.user.id)
    try:
        x = request.user.id
        r=False
        if x is not None:
           ch = User.objects.get(id = x)
           r = ch.hadFilled
    except:
        pass
    context = {
        'videog':videog,
        'count':c,
        'hadFilled':r,
        'cam':cam,
    }
    return render(request,'init/home.html',context)

def setupStudio(request):
    f = VideoGrapherRegisterForm()    
    if request.method == 'POST':
        f = VideoGrapherRegisterForm(request.POST)
        if f.is_valid():
            u = f.save(commit = False)
            u.role = 1
            u.save()
            messages.success(request,"Studio Created Successfully")
            new_user = authenticate(username=f.cleaned_data['username'],
                                    password=f.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/')
        else:
            messages.error(request,f.errors)
    return render(request,'init/setupStudio.html',{'form':f})

@login_required
def studioProfileUpdate(request):
    us = User.objects.get(id = request.user.id)
    if request.user.role == 1:
        f = VideoGrapherProfile(instance=us)
        if request.method == 'POST':
            f = VideoGrapherProfile(request.POST,request.FILES,instance=us)
            if f.is_valid():
                u = f.save(commit = False)
                u.hadFilled = True
                u.save()
                messages.success(request,"Profile Updated Successfully")
                return redirect('home')
    else:
        f = CustomerProfile(instance=us)
        if request.method == 'POST':
            f = CustomerProfile(request.POST,request.FILES,instance=us)
            if f.is_valid():
                u = f.save(commit = False)
                u.hadFilled = True
                u.save()
                messages.success(request,"Profile Updated Successfully")
                return redirect('home')
        messages.error(request,"Something went Wrong...")
    return render(request,'init/studioProfileInfo.html',{"form":f})
    


@login_required
def addCam(request):
    f = CamForm()
    if request.method == 'POST':
        f = CamForm(request.POST,request.FILES)
        if f.is_valid():
            u = f.save(commit = False)
            u.vgId_id = request.user.id
            u.save()
            messages.success(request,"Camera Added Successfully")
            return redirect('home')
    else:
        messages.error(request,"Something Went Wrong...")
    return render(request,'init/addCam.html',{'form':f})
    
@login_required
def editCamdetails(request,id):
    t = CamModels.objects.get(id = id)
    f = CamForm(instance=t)
    if request.method == 'POST':
        f = CamForm(request.POST,request.FILES,instance=t)
        if f.is_valid():
            f.save()
            messages.success(request,"Updated Successfully")
            return redirect('home')
    return render(request,'init/camaraDetails.html',{'form':f})

def viewProfile(request,id):
    data = User.objects.get(id=id)
    cam = CamModels.objects.filter(vgId = id)
    return render(request,'init/viewProfile.html',{'data':data,'cam':cam})

def userReg(request):
    f = UserRegistForm()    
    if request.method == 'POST':
        f = UserRegistForm(request.POST)
        if f.is_valid():
            u = f.save(commit = False)
            u.role = 2
            u.save()
            messages.success(request,"Account Created Successfully")
            new_user = authenticate(username=f.cleaned_data['username'],
                                    password=f.cleaned_data['password1'],
                                   )
            login(request, new_user)
            return redirect('home')
        else:
            messages.error(request,f.errors)
    return render(request,'init/userReg.html',{'form':f})


@login_required
def changepwd(request):
    if request.method =="POST":
        k = PasswordChange(user=request.user,data = request.POST)
        if k.is_valid():
            k.save()
            messages.success(request,"Password Changed Successfully")
            return redirect('/login')
        else:
            messages.error(request,"Can't Change your Password")
    cp = PasswordChange(user = request)
    return render(request,'init/changepwd.html',{'cp':cp})
@login_required
def camview(request,id):
    cam = CamModels.objects.get(id = id)
    return render(request,'init/camview.html',{'data':cam})

def deleteCam(request,id):
    v=CamModels.objects.get(id=id)
    if request.method == 'POST':
        messages.info(request,"Camera Deleted Successfully")
        v.delete()
        return redirect('home')
    
    return render(request,'init/deleteCam.html',{'data':v})

@login_required
def orderform(request,id):
    t = OrderModel.objects.filter(uid_id = request.user.id)
    emp=False
    f = OrderForm()
    if t.count() == 0:
        emp = True
        if request.method == "POST":
            f = OrderForm(request.POST)
            frm = request.POST.get('fromDate')
            to = request.POST.get('toDate')
            c_id = id        
            if f.is_valid():
                u = f.save(commit=False)
                u.cid = c_id
                u.uid_id = request.user.id
                u.uUname = User.objects.get(id = request.user.id).username
                if parseTheEvent(frm,to,c_id):
                    u.save()
                    
                    messages.info(request,"Order recorded Successfully")
                    return redirect('home')
                else:
                    pass
                    messages.warning(request,"Camera is already booked by another person on this period")
    return render(request,'init/orderform.html',{'form':f,'data':emp})
    

def parseTheEvent(a,b,c):
    x = CamModels.objects.get(id = c)
    z = x.bookedDates
    if z == '':
        res = z+a+"_"+b+"/"
    else:
        z.split('/')
        p = a+"_"+b+"/"
        if p in z:
            return False
        else:
            res = z+p
    x.bookedDates = res
    x.save()
    return True

@login_required
def myorders(request):
    lst = []
    emp = True
    ord = OrderModel.objects.all()
    for i in ord:
        cId = i.cid
        cm = CamModels.objects.get(id = cId)
        vid = cm.vgId_id
        if vid == request.user.id:
            lst.append(i)
            emp = False
    if lst == []:
        emp = True
    return render(request,'init/myorders.html',{'data':lst,'emp':emp})

@login_required
def viewCustOrder(request,id):
    t = OrderModel.objects.get(id=id)
    em = t.email
    print(em)
    if request.method == 'POST':
        f = viewCustOrderForm(request.POST,instance=t)
        if f.is_valid():
            u = f.save()
            r = emailSend(request,u.isAccepted,em)
            return redirect('myorders')
    f = viewCustOrderForm(instance=t)
    return render(request,'init/viewCustOrder.html',{'form':f})

def emailSend(request,n,em):
    ls = []
    print(em)
    ls.append(em)
    print('ls',ls)
    if n == 2:
        sd = ls
        print(sd)
        mg = 'Your Order had been Accepted'
        sm = 'Order-ACCEPTED'
        rt = settings.EMAIL_HOST_USER   
        dt = send_mail(sm,mg,rt,sd)
    elif n==3:
        sd = ls
        mg = 'Your Order had been Rejected'
        sm = 'Order-REJECTED'
        rt = settings.EMAIL_HOST_USER   
        dt = send_mail(sm,mg,rt,sd)
    return dt

def mybookings(request):
    t = OrderModel.objects.filter(uid_id = request.user.id)
    emp=False
    if t.count == 0:
        emp = True
    return render(request,'init/mybookings.html',{'emp':emp,'data':t})