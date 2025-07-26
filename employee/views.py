from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import redirect
# Create your views here.

# Create view
def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')  # Redirect to a list view after saving
    else:
        form = EmployeeForm()
    
    return render(request, 'create.html', {'form': form})

# List Employee View
def empoyee_list(request):
    employee = Employee.objects.all()
    return render(request, 'list.html', {'employees': employee})


# Update Employee View
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'update.html', {'form': form})

# Delete Employee View
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('list')
    