from django.urls import path
from .views import register_user
from .views import home
from .views import create_article
from .views import create_order_with_rollback
urlpatterns = [
     path('', home, name='home'),
     #Question 1
     path('register/', register_user, name='register_user'),
     #Question 2
     path('article/', create_article, name='create_article'),
     #Question 3
     path("order/", create_order_with_rollback, name="create_order_with_rollback")
]