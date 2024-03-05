from django.urls import path
from . import views
urlpatterns = [
    path('incomes/', views.incomes_list, name = 'incomes_list'),
    path('incomes/add/', views.IncomeCreateView.as_view(), name='create_income'),
    path('income/<int:pk>/', views.IncomeDetailView.as_view(), name="income_detail_view"),
]