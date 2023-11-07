from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from backapp.models import adminregdb, categorydb, productdb, contactdb, cartdb, userdetails


# Create your views here.
def indexpage(req):
    return render(req,"index.html")
def adadminpage(req):
    return render(req,"adadmin.html")
def saveadminpage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mob = request.POST.get('mobile')
        user = request.POST.get('username')
        password = request.POST.get('password')
        img = request.FILES['image']
        obj = adminregdb(NAME=na, EMAIL=em, MOBILE=mob, USERNAME=user, PASSWORD=password, IMAGE=img)
        obj.save()
        return redirect(adadminpage)
def displayadmin(req):
    data = adminregdb.objects.all()
    return render(req,"displayadmin.html",{'data':data})
def editadmin(req,dataid):
    data = adminregdb.objects.get(id=dataid)
    print(data)
    return render(req,"editadmin.html",{'data':data})
def updateadmin(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        email = req.POST.get('email')
        mob = req.POST.get('mobile')
        uname = req.POST.get('username')
        passwrd = req.POST.get('password')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = adminregdb.objects.get(id=dataid).IMAGE
        adminregdb.objects.filter(id=dataid).update(NAME=na, EMAIL=email, MOBILE=mob, USERNAME=uname, PASSWORD=passwrd, IMAGE=file)
        return redirect(displayadmin)
def deleteadmin(req,dataid):
    data = adminregdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)


def category(req):
    return render(req,"category.html")
def savecategorypage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        dis = request.POST.get('discription')
        img = request.FILES['image']
        obj = categorydb(NAME=na, DISCRIPTION=dis, IMAGE=img)
        obj.save()
        return redirect(category)
def displaycategory(req):
    data = categorydb.objects.all()
    return render(req,"displaycategory.html",{'data':data})
def editcategory(req,dataid):
    data = categorydb.objects.get(id=dataid)
    print(data)
    return render(req,"editcategory.html",{'data':data})
def updatecategorypage(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        dis = req.POST.get('discription')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).IMAGE
        categorydb.objects.filter(id=dataid).update(NAME=na, DISCRIPTION=dis, IMAGE=file)
        return redirect(displaycategory)
def deletecategory(req,dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)


def products(req):
    data = categorydb.objects.all()
    return render(req,"product.html", {'data':data})
def saveproducts(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pri = request.POST.get('price')
        qua = request.POST.get('quantity')
        dis = request.POST.get('discription')
        img = request.FILES['image']
        cat = request.POST.get('category')
        obj = productdb(NAME=na, PRIZE=pri, QUANTITY=qua, DISCRIPTION=dis, CATEGORY=cat, IMAGE=img)
        obj.save()
        return redirect(products)
def displayproduct(req):
    data = productdb.objects.all()
    return render(req, "displayproduct.html", {'data': data})
def editproduct(req,dataid):
    data = productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    print(data)
    print(da)
    return render(req,"editproduct.html", {'datas':data,'da':da})
def updateproduct(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        pri = req.POST.get('price')
        qua = req.POST.get('quantity')
        dis = req.POST.get('discription')
        cat = req.POST.get('category')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).IMAGE
        productdb.objects.filter(id=dataid).update(NAME=na, PRIZE=pri, QUANTITY=qua, DISCRIPTION=dis, CATEGORY=cat, IMAGE=file)
        return redirect(displayproduct)
def deleteproduct(req,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)

def loginpage(req):
    return render(req,"login.html")
def adminlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if User.objects.filter(username__contains = username_r).exists():
            user = authenticate(username = username_r, password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(indexpage)
        else:
            return redirect(loginpage)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
def displaycontactpage(req):
    data = contactdb.objects.all()
    return render(req,"displaycontact.html",{'data':data})


def orderdetails(req):
    data = userdetails.objects.all()
    return render(req, "displayorderdetails.html", {'data': data})
def deleteorderdetails(req,dataid):
    data = userdetails.objects.filter(id=dataid)
    data.delete()
    return redirect(orderdetails)

def displaycartpage(req):
    data = cartdb.objects.all()
    return render(req,"displaycart.html",{'data':data})
def deletecartpage(req,dataid):
    data = cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycartpage)