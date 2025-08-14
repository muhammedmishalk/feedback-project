from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_feedback, name='submit_feedback'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
