from django.urls import path, include
from baseapp import views

app_name = "base"

urlpatterns = [
    path("", views.home, name="homepage"),
    path("login/", views.login_user, name="login_page"),
    path("fin-calculator/", views.fincalc, name="fin_calc"),
    path("investment-calculator", views.investment_calc, name="investment_calc"),
    path("inflation-calculator", views.inflation_calc, name="inflation_calc"),
    path("news", views.news, name="news"),
]
