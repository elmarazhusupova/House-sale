# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login', views.loginPage, name='login'),
#     path('register', views.registerPage, name='register')
# ]


from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    # path('logout/', views.logoutPage, name='logout'),
    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'),
    #      name='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    #      name='password_reset_confirm'),
    # path('reset_password_complete/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    #      name='password_reset_complete'),
    # path('oauth/', include('social_django.urls', namespace='social')),
]
