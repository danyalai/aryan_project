from django.urls import path
from  . import views
urlpatterns = [
    path('http/', views.aryan_http),
    path('dynamic/<days>', views.aryan_dynamic),
]
