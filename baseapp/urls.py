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
    path("percentage-based", views.percent_based, name="percent_based"),
    path("amount-based", views.amount_based, name="amount_based"),
    path("coin-jar-contest", views.coin_jar, name="coin_jar"),
    path("debt-manager", views.debt_manager, name="debt_manager"),
    path("debt-manager/add-loan", views.add_loan, name="add_loan"),
    path("debt-manager/delete-loan/<int:id>", views.delete_loan, name="delete_loan"),
    path("login-user", views.login_user, name="login_user"),
    path("register-user", views.register_user, name="register_user"),
    path("contest-percent-based", views.percent_based_contest_form, name="percent_based_contest_form"),
    path("logout-user", views.logout_user, name="logout_user"),
    path("contest-dashboard", views.contest_dashboard, name="contest_dashboard")
]
