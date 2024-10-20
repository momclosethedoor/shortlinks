from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', index),
    path('shortlinks/create', csrf_exempt(ShortLinksView.as_view()), name='links_create'),
    path('shortlinks/list', links_list, name='links_list'),
    path('<key_url>', get_url)
]