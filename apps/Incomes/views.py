from django.shortcuts import render
from .models import Income

def incomes_list(request):
    incomes = Income.objects.all()
    return render(request, 'incomes/incomes_list.html', {'incomes': incomes})
