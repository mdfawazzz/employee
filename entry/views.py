

# Create your views here.
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def update(request):
    try:
        if request.method == 'POST':
           
            user = Data(id=request.POST['id1'],name=request.POST['name'], department=request.POST['department'], designation=request.POST['designation'], salary=request.POST['salary'], dob=request.POST['dob'], address=request.POST['address'], others=request.POST['others'])
            user.save()
            return redirect('form_view')
    except:
        pass

    data = Data.objects.all().values().order_by('-id')
    return render(request, 'form.html', {'data': data})
def formview(request):
        data=Data.objects.all().values().order_by('-id')
        return render(request,'form.html',{'data':data})
def delete(request):
    try:
        employee = Data.objects.get(id=request.POST['id1'])
        employee.delete()
        data = Data.objects.all().values().order_by('-id')
        return render(request, 'form.html', {'data': data})
    except:
        data=Data.objects.all().values().order_by('-id')
        return render(request,'form.html',{'data':data})
def up(request):
    try:
        employee = Data.objects.get(id=request.POST['id1'])
        new_value = request.POST.get('value')
        print(new_value)
        setattr(employee, request.POST['field'], new_value)
        employee.save()
        data=Data.objects.all().values().order_by('-id')
        return render(request,'form.html',{'data':data})
    except:
        data=Data.objects.all().values().order_by('-id')
        return render(request,'form.html',{'data':data})