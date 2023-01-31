from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache, cache_control

from libraryapp.models import Student, Course, Book, Issue_book


# Create your views here.

def login(request):
    return render(request,'login.html',{'data':''})


def readlog(request):
    name = request.POST['tbname']
    password = request.POST['tbpas']

    user = authenticate(username=name,password=password)
    if user is not None:
        if user.is_superuser:
            return render(request,'home.html')
        else:

            return render(request,'login.html',{'data':'user is not super user...'})

    elif Student.objects.filter(Q(S_name=name) & Q(S_password=password)).exists():
        request.session['n']=name
        return render(request,'stdhome.html',{'name': name})
    else:
        return render(request,'login.html',{'data':'wrong user name and password'})

def adminreg(request):
    return render(request, 'adminreg.html')

def adminred(request):
    name=request.POST['adname']
    email=request.POST['ademail']
    pas=request.POST['adpas']
    if User.objects.filter(Q(username=name) | Q(email=email)).exists():
        return render(request,'adminreg.html',{'data':'username and email is already exists...!'})
    else:
        d=User.objects.create_superuser(username=name,email=email,password=pas)
        d.save()
        return redirect('login')

def studentred(request):
    xname=request.POST['stname']
    xphone = request.POST['stph']
    c1=Course.objects.all()
    if Student.objects.filter(Q(S_phone=xphone) | Q(S_name=xname)).exists():
        return render(request,'studentreg.html',{'data': 'username and email is already exists...!','data1':c1})
    else:
         s = Student()
         s.S_name = request.POST['stname']
         s.S_phone = request.POST['stph']
         s.S_password = request.POST['stpass']
         s.S_semester = request.POST['stsem']
         s.S_course_id = Course.objects.get(course_name=request.POST['ddlcourse'])
         s.save()
         return redirect('login')

def stdregred(request):
    d=Course.objects.all()
    return render(request,'studentreg.html',{'data':'','data1':d})


def addbk_fun(request):
    c=Course.objects.all()
    return render(request,'addbook.html',{'data':c})


def redbk_fun(request):
    c=Book()
    c.B_name=request.POST['bkname']
    c.A_name=request.POST['atname']
    c.Course_id=Course.objects.get(course_name=request.POST['ddlcourse'])
    c.save()
    return redirect('addbk')

def display(request):
    s=Book.objects.all()
    return render(request,'displaybooks.html',{'data':s})


def update(request,id):
    s=Book.objects.get(id=id)
    c = Course.objects.all()
    if request.method == 'POST':
        s.B_name = request.POST['bkname']
        s.A_name = request.POST['atname']
        s.Course_id = Course.objects.get(course_name=request.POST['ddlcourse'])
        s.save()
        return redirect('dis')

    return render(request,'update.html',{'data': s,'data1': c})


def delete(request,id):
    c=Book.objects.get(id=id)
    c.delete()
    return redirect('dis')


def logout(request):
    logout(request)
    return redirect('login')

def assign(request):
    c= Course.objects.all()
    return render(request,'assignbook.html',{'data':c,'data1':'','data2':''})

def redassign(request):
    c = Course.objects.all()
    name=Student.objects.filter(Q(S_semester=request.POST['stsem']) &
                                Q(S_course_id=Course.objects.get(course_name=request.POST['crs'])))
    B=Book.objects.filter(Course_id=Course.objects.get(course_name=request.POST['crs']))
    return render(request,'assignbook.html',{'data2':name,'data1':B,'data':c})

def assignbook(request):
    i = Issue_book()
    i.St_name=Student.objects.get(S_name=request.POST['stname'])
    i.Bk_name=Book.objects.get(B_name=request.POST['bkname'])
    i.I_date = request.POST['st_date']
    i.E_date = request.POST['end_date']
    i.save()
    return redirect('assign')

def issubk(request):
    c=Issue_book.objects.all()
    return render(request,'displayissuebk.html',{'data':c})

def delete1(request,id):
    f=Issue_book.objects.get(id=id)
    f.delete()
    return redirect('issuebk')


def update2(request,id):
    i1=Issue_book.objects.get(id=id)
    s=Student.objects.all()
    b=Book.objects.all()
    if request.method=='POST':
        i1.St_name=Student.objects.get(S_name=request.POST['stname'])
        i1.Bk_name=Book.objects.get(B_name=request.POST['bkname'])
        i1.I_date=request.POST['st_date']
        i1.E_date=request.POST['end_date']
        i1.save()
        return redirect('issuebk')
    return render(request, 'update2.html', {'data1': i1, 's': s, 'b': b})


def call(request):
    s = Issue_book.objects.filter(St_name=Student.objects.get(S_name=request.session['n']))
    return render(request,'studentissuebook.html',{'data':s})


def stdhome(request):
    return render(request,'stdhome.html',{'name':request.session['n']})

def adhome(request):
    return render(request,'home.html')


def disprofile(request):
    s=Student.objects.get(S_name=request.session['n'])
    return render(request,'student profile.html',{'data':s})

def edit(request):
    s=Student.objects.get(S_name=request.session['n'])
    if request.method=='POST':
        s.S_semester = request.POST['stsem']
        s.S_phone = request.POST['stph']
        s.S_password = request.POST['stpass']
        s.save()
        return redirect('profile')
    return render(request,'edit.html',{'data':s})



