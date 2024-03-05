from django.shortcuts import render, redirect
import requests
import json
from baseapp.models import DebtManager

# Create your views here.


def home(request):
    return render(request, "index.html")


def login_user(request):
    return render(request, "login.html")


def fincalc(request):
    return render(request, "fincalc.html")


def investment_calc(request):
    return render(request, "investment_calc.html")


def inflation_calc(request):
    return render(request, "inflation_calc.html")


def news(request):
    with open(
        "C:/Users/mohit/Desktop/I/Projects/FinViser/addons/news_response.json", "r"
    ) as file:
        data = json.load(file)
    articles = data.get("articles", [])
    return render(request, "news.html", {"articles": articles})


def percent_based(request):
    return render(request, "percent_based.html")


def amount_based(request):
    return render(request, "amount_based.html")

def coin_jar(request):
    print("Coin jar started")
    pass


def debt_manager(request):
    loans = DebtManager.objects.all()
    return render(request, "debtmanager.html", {"loans": loans})


def add_loan(request):
    if request.method == "POST":
        loan_type = request.POST.get("loan_type")
        loan_amount = request.POST.get("loan_amount")
        due_date = request.POST.get("due_date")
        DebtManager.objects.create(
            loan_type=loan_type, loan_amount=loan_amount, due_date=due_date
        )
        return redirect("base:debt_manager")
    pass


def delete_loan(request, id):
    loan = DebtManager.objects.get(pk=id)
    loan.delete()
    return redirect("base:debt_manager")


# def news(request):
#     url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=adbf30f0346943d2b2cd50b2928e618e"
#     response = "../addons/news_response.json"
#     response = requests.get(url)
#     context = {}
#     if response.status_code == 200:
#         data = response.json()
#         context["news_data"] = data["articles"]
#     else:
#         context["error"] = f"Error : {response.status_code}"
#         for i in data["articles"]:
#             print(i)
#             print()
#             print()

#     return render(request, "news.html", context)


# def news(request):
#     response = "../addons/news_response.json"
#     data = response.json()
#     context = {"news_data": data["articles"]}
#     print(context)
#     return render(request, "news.html")


# views.py


# def future_value_adjusted_for_inflation(present_value, inflation_rate, years):
#     future_value = present_value * (1 + inflation_rate) ** years
#     return future_value


# # Example usage:
# present_value = 10000  # Current amount of money
# inflation_rate = 0.06  # Annual inflation rate (6% for India)
# years = 10  # Number of years into the future

# future_value = future_value_adjusted_for_inflation(present_value, inflation_rate, years)
# print(
#     f"The future value adjusted for inflation after {years} years would be ₹{future_value:.2f}"
# )
