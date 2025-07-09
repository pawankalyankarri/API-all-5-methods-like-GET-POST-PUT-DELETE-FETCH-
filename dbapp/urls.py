from django.urls import path
from . import views

urlpatterns = [
    path('insert/',views.Insert.as_view(),name='inserturl'),
    path('select/',views.Select.as_view(),name='selecturl'),
    path('update/<int:pk>/',views.Update.as_view(),name='updateurl'),
    path('delete/<int:pk>/',views.Delete.as_view(),name='deleteurl')
    
]