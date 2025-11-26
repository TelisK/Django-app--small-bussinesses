from django.shortcuts import render
from .models import Income
# Create your views here.
def index(request):
    all_income = Income.objects.all()
    return render(request,'income_expenses/index.html',{'all_income':all_income})
