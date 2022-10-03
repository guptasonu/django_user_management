from django.urls import path, include
from accounts.views import SignUpView, ProfileView, UserListView, UserDetailsView

urlpatterns = [
    path("", UserListView.as_view(), name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile_details/<int:pk>/", UserDetailsView.as_view(), name="details"),
    path("accounts/profile/<int:pk>/", ProfileView.as_view(), name="profile"),
]
