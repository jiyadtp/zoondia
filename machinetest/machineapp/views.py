import pyshorteners as pyshorteners
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from . models import *
import re
import qrcode

# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user_details = Users.objects.filter(email=email).first()
        if user_details:
            return redirect('dashboard')
        else:
            messages.error(request, str("Invalid Credentials"))
            return redirect(request.META['HTTP_REFERER'])
    return render(request,'login.html')

def login_check(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    user = Users.objects.filter(email=email).first()
    print("mmm",user.password)
    if not user:
        return JsonResponse({"message": "Invalid Datas", "status": "error"})
    elif user.password != password:
        return JsonResponse({"message": "Invalid Password", "status": "error"})
    else:
        request.session['user_id'] = user.id
        return JsonResponse({"message": "success", "status": "success"})

def register(request):
    if request.method == "POST":
        messages.success(request, str("Successfully Registered"))
        return redirect("/")
    return render(request,'register.html')

def register_data(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname").strip()
        lastname = request.POST.get("lastname").strip()
        email = request.POST.get("email").strip()
        password = request.POST.get("password").strip()
        confirm_password = request.POST.get("confirm_password").strip()
        required_fields = []
        if not firstname:
            required_fields.append("First Name")
        if not email:
            required_fields.append("Email")
        if not password:
            required_fields.append("Password")
        if not confirm_password:
            required_fields.append("Confirm Password")
        if required_fields:
            response = f"{', '.join(required_fields)} are required"
            return JsonResponse({"message": response, "status": "error"})
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return JsonResponse({"message": "not a valid email", "status": "error"})
        if Users.objects.filter(email=email).exists():
            return JsonResponse({"message": "Email Already Exists", "status": "error"})
        if password != confirm_password:
            return JsonResponse({"message": "Password Doest not Match", "status": "error"})
        if not re.search('[A-Z]', password) or not re.search('[0-9]', password) or not re.search('[!@#$%^&*(),.?":{}|<>]', password) or len(password) < 8:
            return JsonResponse({"message": "Password does not match the format", "status": "error"})
        data_create = Users.objects.create(
            firstname = firstname,
            lastname = lastname,
            email = email,
            password = password
        )
        return JsonResponse({"message": "success", "status": "success"})



def dashboard(request):
    user_id = request.session['user_id']
    data = UrlDetails.objects.filter(user_id_id=user_id)
    context = {
        'data':data
    }
    return render(request,"dashboard.html",context)

def create_url(request):
    url_name = request.POST.get("url_name").strip()
    required_fields = []
    if not url_name:
        required_fields.append("Url Name")
    if required_fields:
        response = f"{', '.join(required_fields)} are required"
        return JsonResponse({"message": response, "status": "error"})
    short_url = pyshorteners.Shortener()
    shortened = short_url.tinyurl.short(url_name)
    # qr_value = url_name.split("/")
    # value1 = shortened
    # QRcode = qrcode.QRCode(
    #     error_correction=qrcode.constants.ERROR_CORRECT_H
    # )
    # QRcode.add_data(value1)
    # QRcode.make()
    # QRimg = QRcode.make_image(back_color="white")
    # QRimg.save('./qr_image/' + str(qr_value) + '.png')
    # import os
    # import base64
    # url1 = './qr_image/' + str(qr_value) + '.png'
    # with open(url1, "rb") as image_file:
    #     encoded_string = base64.b64encode(image_file.read())
    #     output = encoded_string.decode()
    # os.remove(url1)
    # os.remove('./qr_image/' + str(qr_value) + '1.jpeg')
    user_id = request.session['user_id']
    data = UrlDetails.objects.create(user_id_id=user_id, url=shortened)
    messages.success(request, str("Successfully Created"))
    return redirect(request.META['HTTP_REFERER'])


def edit_url(request):
    id = request.GET.get("id")
    data = UrlDetails.objects.get(id=id)
    print("data",data)
    context = {
        'data':data
    }
    return render(request,"edit_url.html",context)

def update_url(request):
    url_id = request.POST.get("url_id")
    url_name = request.POST.get("url_name").strip()
    required_fields = []
    if not url_name:
        required_fields.append("Url Name")
    if required_fields:
        response = f"{', '.join(required_fields)} are required"
        return JsonResponse({"message": response, "status": "error"})
    short_url = pyshorteners.Shortener()
    shortened = short_url.tinyurl.short(url_name)
    # qr_value = url_name.split("/")
    # value1 = shortened
    # QRcode = qrcode.QRCode(
    #     error_correction=qrcode.constants.ERROR_CORRECT_H
    # )
    # QRcode.add_data(value1)
    # QRcode.make()
    # QRimg = QRcode.make_image(back_color="white")
    # QRimg.save('./qr_image/' + str(qr_value) + '.png')
    # import os
    # import base64
    # url1 = './qr_image/' + str(qr_value) + '.png'
    # with open(url1, "rb") as image_file:
    #     encoded_string = base64.b64encode(image_file.read())
    #     output = encoded_string.decode()
    # os.remove(url1)
    # os.remove('./qr_image/' + str(qr_value) + '1.jpeg')
    user_id = request.session['user_id']
    data = UrlDetails.objects.create(user_id_id=user_id, url=shortened)
    messages.success(request, str("Successfully Created"))
    return redirect(request.META['HTTP_REFERER'])



def delete_url(request,id):
    print("llll",id)
    data = UrlDetails.objects.get(id=id)
    print("llll", data)
    data.delete()
    messages.success(request, str("Successfully Deleted"))
    return redirect(request.META['HTTP_REFERER'])