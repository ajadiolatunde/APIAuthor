from django.urls import  path, reverse
from . import views

app_name = 'author'

urlpatterns = [
    path('a/<int:id>',views.authorlist, name='author_list'),
    path('a/login', views.login_view, name='login_view'),

]
