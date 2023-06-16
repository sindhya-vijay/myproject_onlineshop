from django.shortcuts import render, redirect
from myapp.models import category_db, productdb, contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def homepage(request):
    return render(request, "index.html")

def category_page(req):
    return render(req, "Add category.html")


def category_data(req):
    if req.method == "POST":
        na = req.POST.get('name')
        ds = req.POST.get('descr')
        img = req.FILES['image']
        obj = category_db(Name=na, Description=ds, Image=img)
        obj.save()
        messages.success(req, "Category saved successfully..!")
        return redirect(category_page)

def Display_category(request):
    data = category_db.objects.all()
    return render(request, "Display category.html", {'data': data})


def Edit_category(req, dataid):
    data = category_db.objects.get(id=dataid)
    return render(req, "Edit category.html", {'data': data})


def Update_category(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        dsr = request.POST.get('descr')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = category_db.objects.get(id=dataid).Image

        category_db.objects.filter(id=dataid).update(Name=na, Description=dsr, Image=file)
        messages.success(request, "Edited successfully")
        return  redirect("Display_category")

def Delete_category(request, dataid):
    data = category_db.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted")
    return redirect(Display_category)

def Add_product(request):
    data = category_db.objects.all()
    return render(request, "Add product.html", {'data':data})

def productdata(request):
    if request.method == "POST":
        ct = request.POST.get('cname')
        pna = request.POST.get('pname')
        pr = request.POST.get('price')
        brd = request.POST.get('brand')
        ds = request.POST.get('descr')
        img = request.FILES['image']
        obj = productdb(Category=ct,Product=pna,Price=pr,Brand=brd, Description=ds, Image=img)
        obj.save()
        messages.success(request, "Product saved successfully..!")
        return redirect("Add_product")

def productdisplay(request):
    data = productdb.objects.all()
    return render(request, "Display product.html", {'data':data})

def Edit_product(request, dataid):
    cat = category_db.objects.all()
    pro = productdb.objects.get(id=dataid)
    return render(request, "Edit product.html",{'cat':cat, 'pro':pro})

def Update_product(request, dataid):
    if request.method == "POST":
        if request.method == "POST":
            ct = request.POST.get('cname')
            pna = request.POST.get('pname')
            pr = request.POST.get('price')
            brd = request.POST.get('brand')
            ds = request.POST.get('descr')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image

        productdb.objects.filter(id=dataid).update(Category=ct, Product=pna,Price=pr,Brand=brd,Description=ds, Image=file)
        return redirect("productdisplay")

def Delete_product(req, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect("productdisplay")

def Loginpage(request):
    return render(request, "Login_page.html")

def adminlogin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pswd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pswd)

            if user is not None:
                login(request, user)
                request.session['username'] = uname
                request.session['password'] = pswd
                messages.success(request, "Login successfully")
                return redirect(homepage)
            else:
                messages.error(request, "Invalid username or password")
                return redirect(homepage)
        else:
            messages.error(request, "Invalid username or password")
            return redirect(Loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Succesfully logout")
    return redirect("Loginpage")


def contact_display(request):
    data = contactdb.objects.all()
    return render(request, "Display_contact.html", {'data': data})





