from django.shortcuts import render,redirect
from MyApp.models import Employee
from MyApp.forms import EmployeeForm

# Create your views here.

def show_view(request):
    employees=Employee.objects.all().order_by('eno')
    return render(request,'MyApp/index.html',{'employees':employees})

def create_view(request):
    formobj=EmployeeForm()
    if request.method=='POST':
        formobj=EmployeeForm(request.POST)
        if formobj.is_valid():
            print('Successfully  Entered ')
            formobj.save()
            return redirect('/index')
    return render(request,'MyApp/create.html',{'form1':formobj})

def delete_view(request,pk):
    employees=Employee.objects.get(id=pk)
    employees.delete()
    return redirect('/index')

def update_view(request,pk):
    employees = Employee.objects.get(id=pk)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employees)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request,'MyApp/update.html',{'employees':employees})