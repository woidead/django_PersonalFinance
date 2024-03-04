from django.urls import path
from . import views
urlpatterns = [
    path('incomes/', views.incomes_list, name = 'incomes_list')
]