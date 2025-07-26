from django.urls import path
from . import views

urlpatterns = [
    path("", views.empoyee_list, name="list"),  # Home view for employee app
    path("create/", views.create_employee, name="create"),  # Create employee view
    path("update/<int:pk>/", views.update_employee, name="update"),  # Update employee view
    path("delete/<int:pk>/", views.delete_employee, name="delete"),  # Delete employee view
]
