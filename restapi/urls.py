from django.urls import path
from . import views

urlpatterns = [
    path('getemp/',views.GetEmployee),
    path('modifyemp/<int:pk>/',views.ModifyEmp)
]