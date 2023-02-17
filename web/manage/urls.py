from django.urls import path
from .views.product import ProductIndexView
from .views.dashboard import DashboardIndexView

urlpatterns = [
    path('dashboard', DashboardIndexView.as_view(), name='index'),
    path('products', ProductIndexView.as_view(), name='index')
]
