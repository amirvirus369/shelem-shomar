from django.urls import path
from . import views
app_name = 'shelem_main'
urlpatterns = [
    path('shelem/<int:id>',views.shelem_main,name='main_shelem_url'),
    path('shelem_joker/<int:id>',views.shelem_joker,name='shelem_joker'),
    path('win/<int:id>',views.win_shelem,name='win_shelem'),
    path('history',views.history,name='history'),
    path('delete/<int:id>',views.delete_last_cart,name='delete'),
    path('edit/<int:id>',views.edit_game,name='edit'),
    path('edit_joker/<int:id>',views.edit_game_joker,name='edit_joker'),
    path('',views.register,name='reg'),
    path('type',views.game_type,name='type'),
    path('del/<int:id>',views.del_table,name='del')
]