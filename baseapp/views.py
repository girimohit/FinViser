from django.shortcuts import render, redirect
import requests
import json
from baseapp.models import DebtManager
from django.contrib.auth.models import User
from baseapp.models import CustomUser, Contest
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, "index.html")


def register_user(request):
    if request.method == "POST":
        # Extract form data
        username = request.POST.get("username")
        full_name = request.POST.get("full_name")
        age = request.POST.get("age")
        phone_number = request.POST.get("phone_number")
        upi_id = request.POST.get("upi_id")
        pan = request.POST.get("pan")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            # Passwords don't match, handle this error accordingly
            # return render(
            #     request, "auth/signup.html", {"error": "Passwords do not match"}
            # )
            return HttpResponse("Password doesn't match")

        # Create new CustomUser instance
        new_user = CustomUser(
            username=username,
            email=email,
            full_name=full_name,
            age=age,
            phone_number=phone_number,
            upi_id=upi_id,
            pan=pan,
        )
        new_user.set_password(
            password
        )  # Manually set the password (don't forget this step)
        new_user.save()

        # Log the user in
        login(request, new_user)

        # Redirect to some success page
        return redirect("base:homepage")

    return render(request, "auth/signup.html")


def login_user(request):
    if request.method == "POST":
        # Extract username and password from the form
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate userF
        user = authenticate(request, username=username, password=password)

        # Check if user authentication is successful
        if user is not None:
            # Log the user in
            login(request, user)

            # Redirect to some success page
            return redirect("base:homepage")
        else:
            # Authentication failed, handle this error accordingly
            return render(request, "auth/login.html", {"error": "Invalid credentials"})

    return render(request, "auth/login.html")


def logout_user(request):
    logout(request)
    return redirect("base:homepage")


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


@login_required
def contest_dashboard(request):
    return HttpResponse("Dashboard Here!!!")


@login_required
def percent_based_contest_form(request):
    if request.method == "POST":
        # upi_id = request.user.upi_id
        monthly_income = request.POST.get("monthly_income")
        desired_saving = request.POST.get("desired_saving")
        print(monthly_income)
        print(desired_saving)
        obj = Contest(
            user=request.user,
            monthly_income=monthly_income,
            desired_saving=desired_saving,
        )
        obj.save()
        return redirect("base:contest_dashboard")
    return render(request, "percent_contest_form.html")
