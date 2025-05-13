from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),     # 여기에 동작코드
    path('logout/', views.logout_view, name='logout'),  # 여기에 동작코드
    path('home/', views.home_view, name='home'),        # 여기에 동작코드
]
