from django.shortcuts import render,redirect
from backapp.models import categorydb, productdb, contactdb, cartdb, userdetails
from frontapp.models import userlogindb
from django.contrib import messages


# Create your views here.
def homepage(req):
    data = categorydb.objects.all()
    da = productdb.objects.all()
    return render(req,"home.html",{'data':data,'da':da})

def contactpage(req):
    return render(req,"contact.html")

def aboutuspage(req):
    return render(req,"aboutus.html")

def shoppage(req):
    da=categorydb.objects.all()
    return render(req,"shop.html",{'da':da})
def blogpagee(req):
    data=categorydb.objects.all()
    return render(req,"blog.html",{'data':data})

def prod(req,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = productdb.objects.filter(CATEGORY=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(req,"products.html",context)
def productsingle(req,dataid):
    data=productdb.objects.get(id=dataid)
    return render(req,"singleproduct.html",{"dat":data})
def savecontactpage(request):
    if request.method == "POST":
        em = request.POST.get('email')
        mes = request.POST.get('message')
        obj = contactdb(EMAIL=em, MESSAGE=mes)
        obj.save()
        return redirect(contactpage)

def userloginpage(req):
    return render(req,"userlogin.html")
def saveuserlogin(request):
    if request.method == "POST":
        em = request.POST.get('email')
        us = request.POST.get('username')
        pas = request.POST.get('password')
        cpas = request.POST.get('cpass')
        if pas == cpas:
            obj = userlogindb(EMAIL=em, USERNAME=us, PASSWORD=pas,CONFIRMPASSWORD=cpas)
        obj.save()
        messages.success(request,"Registered Successfully..!")
        return redirect(userloginpage)

def custemerlogin(request):
    if request.method=='POST':
        Username_r=request.POST.get("username")
        Password_r=request.POST.get("password")

        if userlogindb.objects.filter(USERNAME=Username_r,PASSWORD=Password_r).exists():
            request.session['username']=Username_r
            request.session['password']=Password_r
            messages.success(request, "Login Successfully...!")
            return redirect(homepage)
        else:
            messages.error(request,"Invalid User..!")
            return render(request,'userlogin.html')

def userlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully...!")
    return redirect(userloginpage)

def savecartpage(req):
    if req.method == "POST":
        na = req.POST.get('name')
        qty = req.POST.get('quantity')
        tprice = req.POST.get('totalprice')
        price = req.POST.get('price')
        obj = cartdb(NAME=na, QUANTITY=qty, TPRIZE=tprice, PRIZE=price)
        obj.save()
        messages.success(req,"Add To Cart Successfully...!")
        return redirect(homepage)


def cartpage(req):
    data = cartdb.objects.all()
    return render(req,"cart.html",{'data':data})

def deletecartitem(req,dataid):
    data = cartdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Deleted Successfully...!")
    return redirect(cartpage)

def checkoutpage(req):
    data = cartdb.objects.all()
    return render(req,"checkout.html",{'data':data})
def saveuserdetails(request):
    if request.method == "POST":
        na = request.POST.get('name')
        qua = request.POST.get('address')
        dis = request.POST.get('state')
        email = request.POST.get('email')
        pdt = request.POST.get('pdtname')
        prize = request.POST.get('prize')
        obj = userdetails(NAME=na, ADDRESS=qua, STATE=dis,EMAIL=email,PRODUCT=pdt,PRIZE=prize)
        obj.save()
        messages.success(request, "Order Successfully...!")
        return redirect(homepage)


