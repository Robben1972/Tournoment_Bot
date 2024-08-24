from rest_framework import serializers
from .models import Player, Winner, Opponent, Looser, Reward


class PlayerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class RewardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'


class WinnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = '__all__'


class OpponentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Opponent
        fields = '__all__'


class LooserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Looser
        fields = '__all__'
