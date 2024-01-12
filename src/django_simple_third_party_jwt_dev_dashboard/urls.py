from django.urls import path

from django_simple_third_party_jwt_dev_dashboard import views

urlpatterns = [
    path("", views.dashboard, name="dev-dashboard"),
    path("login", views.login, name="dev-session-login"),
    path("logout", views.session_logout, name="dev-session-logout")
]
