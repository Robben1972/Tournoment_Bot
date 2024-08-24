import os

from django.db import models
from django.db.models.signals import post_save
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("REGISTRATION_TOKEN")


# Create your models here.
class Player(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.IntegerField(unique=True)
    fullname = models.CharField(max_length=40)
    nickname = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=5)

    def __str__(self):
        return self.fullname


class Winner(models.Model):
    user_id = models.IntegerField()
    fullname = models.CharField(max_length=40)
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname


def save_winner(sender, instance, **kwargs):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={instance.user_id}&text={f"*Tabriklaymiz {instance.nickname}* Siz keyingi bosqichdasiz"}&parse_mode=markdown'
    response = requests.get(url)


class Looser(models.Model):
    user_id = models.IntegerField()
    fullname = models.CharField(max_length=40)
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname


def save_looser(sender, instance, **kwargs):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={instance.user_id}&text={f"*Siz yutqazdingiz b* Hech qisi yoq keyingi safar omadingiz keladi"}&parse_mode=markdown'
    response = requests.get(url)


class Reward(models.Model):
    user_id = models.IntegerField()
    fullname = models.CharField(max_length=40)
    nickname = models.CharField(max_length=20)
    status = models.CharField(max_length=5)

    def __str__(self):
        return self.fullname


def save_reward(sender, instance, **kwargs):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={instance.user_id}&text={f"Hurmatli {instance.fullname}({instance.nickname}). Siz {instance.status}-orinni olganizni aytishdan mamnunmiz 🏆🏆"}&parse_mode=markdown'
    response = requests.get(url)


class Opponent(models.Model):
    user_id = models.IntegerField()
    nickname = models.CharField(max_length=20)
    opponent_nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname


def save_opponent(sender, instance, **kwargs):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={instance.user_id}&text={f"Hozir sizning navbatingiz va sizning raqibingiz *{instance.opponent_nickname}*"}&parse_mode=markdown'
    response = requests.get(url)


post_save.connect(save_winner, sender=Winner)
post_save.connect(save_opponent, sender=Opponent)
post_save.connect(save_looser, sender=Looser)
post_save.connect(save_reward, sender=Reward)
