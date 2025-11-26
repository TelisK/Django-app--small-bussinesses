from django.shortcuts import render
from .models import Income, Expenses
# Create your views here.
def income(request):
    all_income = Income.objects.all()
    return render(request,'income_expenses/income.html',{'all_income':all_income})

def expenses(request):
    all_expenses = Expenses.objects.all()
    return render(request,'income_expenses/expenses.html',{'all_expenses':all_expenses})