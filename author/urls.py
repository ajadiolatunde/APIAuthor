from django.urls import  path, reverse
from . import views

app_name = 'author'

urlpatterns = [
    path('a/<int:id>',views.authorlist, name='author_list'),
    path('a/login', views.login_view, name='login_view'),
    path('a/ses', views.get_session, name='ses_view'),
    path('a/token', views.token, name='token_view'),

]
