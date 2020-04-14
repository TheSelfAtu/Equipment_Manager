from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
    path('equip_add', views.EqAdd.as_view(), name='equip_add'),
    path('equip_update/<int:pk>', views.EqUpdate.as_view(), name='equip_update'),
    path('user_add', views.UserAdd, name='user_add'),
    path('user_update/<int:pk>', views.UserUpdate.as_view(), name='user_update'),

]