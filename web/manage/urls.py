from django.urls import include, path
from django.views.i18n import set_language

from .views import product, dashboard, category
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

    #dashbaord
    path('dashboard/', dashboard.DashboardIndexView.as_view(), name='dashboard/index'),

    # category
    path('categories/', category.CategoryIndexView.as_view(), name='categories/index'),
    path('categories/create/', category.CategoryCreateView.as_view(), name='categories/create'),

    # product
    path('products/', product.ProductIndexView.as_view(), name='products/index'),

    path('i18n/', include('django.conf.urls.i18n'))
]
