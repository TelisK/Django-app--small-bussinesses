from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('income/',views.income, name='income'),
    path('expenses/',views.expenses, name='expenses'),
]