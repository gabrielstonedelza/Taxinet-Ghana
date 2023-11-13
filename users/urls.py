from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', views.home, name="home"),
    path('get_user/', views.get_user),

    path('search_users/', views.GetAllUsers.as_view()),
    path('users/', views.AllUsers.as_view()),

    path('update_username/', views.update_username),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='taxinet_users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='taxinet_users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='taxinet_users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='taxinet_users/password_reset_complete.html'), name='password_reset_complete'),

    path('update_blocked/<int:id>/', views.update_blocked),
    path('get_all_blocked_users/', views.get_all_blocked_users),
]
