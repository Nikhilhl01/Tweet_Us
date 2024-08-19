from django.urls import path
from . import views

urlpatterns = [
    # path('', admin.site.urls),
    path('', views.tweet_list, name = 'tweet_list'),
    path('create/', views.tweet_create, name = 'tweet_create'),
    path('<int:id>/edit/', views.tweet_edit, name = 'tweet_edit'),
    path('<int:id>/delete/', views.tweet_del, name = 'tweet_del'),
    path('register/', views.reg, name = 'reg'),
    # path('', views.index, name = 'index'),
]
