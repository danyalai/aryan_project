from django.urls import path
from  . import views
urlpatterns = [
    path('http/', views.aryan_http),
    path('dynamic/<day>', views.aryan_dynamic),
]
