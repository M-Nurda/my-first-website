from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.post_list, name='index'),
    path('', views.home_page, name='confirm'),
]
    # path('', views.Homeview.as_view(), name='post_list'),
    # path('', views.Homeview.as_view(), name='save_client'),