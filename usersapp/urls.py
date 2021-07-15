from django.urls import path
from usersapp.views import RegUserView, LoginUserView, logout_user
from django.contrib.auth import views as auth_views
from postiks.settings import EMAIL_HOST_USER

urlpatterns = [
    path("login/", LoginUserView.as_view(), name="login-page"),
    path("register/", RegUserView.as_view(), name="reg-page"),
    path("logout/", logout_user, name="logout-page"),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            email_template_name="registration/password_reset_email.html",
            from_email=EMAIL_HOST_USER,
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
