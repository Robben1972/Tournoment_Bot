from django.urls import path
from .views import PlayerView, PlayerDetailView, WinnerView, OpponentView, LooserView, RewardView

urlpatterns = [
    path('player/', PlayerView.as_view()),
    path('winner/', WinnerView.as_view()),
    path('looser/', LooserView.as_view()),
    path('opponent/', OpponentView.as_view()),
    path('reward/', RewardView.as_view()),
    path('player/<int:pk>/', PlayerDetailView.as_view()),
]
