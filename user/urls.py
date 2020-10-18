from django.urls import path

from .views import RegisterUserView

urlpatterns = [
    path('register', RegisterUserView.as_view(extra_context={"action": "Sign Up"}))
]
