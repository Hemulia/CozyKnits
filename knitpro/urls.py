from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    YarnCreateView,
    YarnListView,
    YarnUpdateView,
    RegisterView,
)

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('project/new', ProjectCreateView.as_view()),
    path('project/<int:pk>', ProjectUpdateView.as_view()),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view()),
    path('yarn/new', YarnCreateView.as_view()),
    path('yarn/', YarnListView.as_view()),
    path('yarn/<int:pk>', YarnUpdateView.as_view()),
    
    path('registration', RegisterView.as_view()),
	path('login', LoginView.as_view(next_page="/")),
	path('accounts/login/', LoginView.as_view(next_page="/")),
	path('logout', LogoutView.as_view(next_page="/")),
]
