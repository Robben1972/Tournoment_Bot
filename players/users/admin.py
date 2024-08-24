from django.contrib import admin
from .models import Player, Winner, Opponent, Looser, Reward


# Register your models here.

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'fullname', 'nickname', 'phone_number', 'status')


@admin.register(Reward)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'fullname', 'nickname', 'status')


@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'fullname', 'nickname')


@admin.register(Looser)
class LooserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'fullname', 'nickname')


@admin.register(Opponent)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'nickname', 'opponent_nickname')
