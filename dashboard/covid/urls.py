from django.urls import path
from covid import views


urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard')
]
