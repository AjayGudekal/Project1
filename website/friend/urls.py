from django.conf.urls import url
# from django.contrib import admin
from .views import Test3

urlpatterns=[

    url(r'^test3/',Test3),
]