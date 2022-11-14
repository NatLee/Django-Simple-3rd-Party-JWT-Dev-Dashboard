from django.urls import path

from django_simple_third_party_jwt_dev_dashboard import views

urlpatterns = [
    path("", views.dashboard, name="dev_dashboard"),
    path("login", views.jwt_login, name="dev_jwt_login"),
]
