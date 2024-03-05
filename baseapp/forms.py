# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
# from baseapp.models import CustomUser


# class SignUpForm(UserCreationForm):
#     # email = forms.EmailField(max_length=200, help_text="Required")
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Username"}),
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={"placeholder": "Email"}), required=False
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
#         max_length=16,
#         required=True,
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
#         max_length=16,
#         required=True,
#     )

#     class Meta:
#         model = CustomUser
#         fields = (
#             "username",
#             "full_name",
#             "age",
#             "phone_number",
#             "upi_id",
#             "pan",
#             "email",
#             "password1",
#             "password2",
#         )
