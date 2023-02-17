from django.urls import path

from .views import product, dashboard
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views

app_name = 'manage'

urlpatterns = [
    # auth
    path('auth/login/', auth_views.LoginView.as_view(
        template_name='auth/login.html',
        authentication_form=AuthenticationForm
    ), name='auth/login'),
    path('auth/logout/', auth_views.LogoutView.as_view(
        next_page='manage:auth/login'
    ), name='auth/logout'),
    path('auth/forgot-password/', auth_views.PasswordResetView.as_view(
        template_name='auth/forgot_password.html',
        # email_template_name='backend/user/forgot_password_email.html',
        # subject_template_name='backend/user/forgot_password_subject.txt',
        success_url='complete/',
    ), name='auth/forgot_password'),
    path('auth/forgot-password/complete/', auth_views.PasswordResetDoneView.as_view(
        template_name='auth/forgot_password_complete.html'
    ), name='user/forgot_password_complete'),

    path('dashboard/', dashboard.DashboardIndexView.as_view(), name='dashboard/index'),
    path('products/', product.ProductIndexView.as_view(), name='products/index')
]
