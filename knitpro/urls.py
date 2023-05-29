from django.urls import path
from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    YarnCreateView,
    YarnListView,
    YarnUpdateView,
)

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('project/new', ProjectCreateView.as_view()),
    path('project/<int:pk>', ProjectUpdateView.as_view()),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view()),
    path('yarn/new', YarnCreateView.as_view()),
    path('yarn/', YarnListView.as_view()),
    path('yarn/<int:pk>', YarnUpdateView.as_view()),
]
