from django.conf.urls.static import static
from django.urls import path
from .views import base

urlpatterns = [
    path('', base.index, name='index'),
]
