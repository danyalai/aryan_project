from django.urls import path
from  . import views
urlpatterns = [
    path('', views.days_list),
    path('http/', views.aryan_http),
    path('dynamic/<day>', views.aryan_dynamic),
]
