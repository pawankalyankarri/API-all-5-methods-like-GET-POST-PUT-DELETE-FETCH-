from django.urls import path
from . import views

urlpatterns = [
    path('getemployee/',views.GetEmployee),
    path('modifyemployee/<int:pk>/',views.ModifyEmployee)
]