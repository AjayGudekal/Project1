from django.conf.urls import url
# from django.contrib import admin
from .views import Test2,Empdata

urlpatterns=[

    url(r'^test2/',Test2),
    url(r'^employee/',Empdata),
]