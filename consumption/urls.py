from django.urls import path
from .views import index, register_view, login_view, choose_category, detail_view

app_name = 'consumption'

urlpatterns = [
    path('detail/<int:user_id>/', detail_view, name='detail'),
    path('category/', choose_category, name='category'),
    path('aut/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('', index, name='index'),

]
