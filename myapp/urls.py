# from django.urls import path
# from . import views
#
#
#
#
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('delete/<int:id>/', views.delete_book, name='delete_book')
#
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_page, name='signup_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_user, name='logout_user'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
]
