from .models import Player, Winner, Opponent, Looser, Reward
from rest_framework import generics
from .serializers import PlayerSerializers, WinnerSerializers, OpponentSerializers, LooserSerializers, RewardSerializers


# Create your views here.

class PlayerView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializers


class WinnerView(generics.ListCreateAPIView):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializers


class LooserView(generics.ListCreateAPIView):
    queryset = Looser.objects.all()
    serializer_class = LooserSerializers


class RewardView(generics.ListCreateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializers


class OpponentView(generics.ListCreateAPIView):
    queryset = Opponent.objects.all()
    serializer_class = OpponentSerializers


class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializers
