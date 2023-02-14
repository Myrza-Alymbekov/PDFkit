from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns = [
    # path('main/', views.main_page, name='main'),
    path('pdf/', views.users_pdf, name='pdf'),
    # path('pdf/', views.html_to_pdf, name='pdf'),
    path('list/', views.UserListView.as_view(), name='users_list'),
    path('create/', views.UserCreateView.as_view(), name='users_create'),
]
