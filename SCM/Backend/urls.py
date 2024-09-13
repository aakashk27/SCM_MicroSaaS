from django.contrib import admin
from django.urls import include, path

urlpatterns = [
   path('company/', include('Backend.Company.urls')),

]