from django.contrib import admin
from .models import main,game
# Register your models here.
class main_game_admin(admin.TabularInline):
    model = game


@admin.register(main)
class game_admin(admin.ModelAdmin):
    inlines = (main_game_admin,)