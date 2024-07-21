from django.shortcuts import render,redirect
from django.http import HttpResponse
from ems.models import Employee

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def view_home(request):
    emps = Employee.objects.all()
    return render(request,'ems/home.html',{'emps':emps})

def view_add_emp(request):
    if request.method=='POST':
        # print('data is coming')
        # fetch the data
        name = request.POST.get('name')
        id = request.POST.get('id')
        contact = request.POST.get('contact')
        working = request.POST.get('working')
        department = request.POST.get('department')
        address = request.POST.get('address')

        # Create the object and set the data
        emp = Employee()
        emp.name = name
        emp.id = id
        emp.contact = contact
        
        if working is None:
            emp.working=False
        else:
            emp.working=True

        emp.department = department
        emp.address = address

        # save the data
        emp.save()
        return redirect('/ems/home/')

    return render(request,'ems/addemp.html')

def view_delete_emp(request,id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect('/ems/home/')

def view_update_emp(request,id):
    emp = Employee.objects.get(pk=id)
    return render(request,'ems/updateemp.html',
                  {'emp':emp})

def view_signup(request):
    if request.method=='POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password!=cpassword:
            return HttpResponse('Your Password Did not Matched!')
        else:

            my_user = User.objects.create_user(username,password)
            my_user.save()
            return redirect("/ems/login/")
    return render(request,'ems/signup.html')

def view_login(request):
    if request.method=='POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        # Match user model and signup form data
        my_user = authenticate(request,name=username,password=password)

        if my_user is None:
            return HttpResponse('Username or password did not matched')
        else:
            login(request,my_user)
            return redirect('/ems/add-emp/')
            
        
    return render(request,'ems/login.html')