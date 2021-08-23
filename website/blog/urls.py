from django.conf.urls import url
# from django.contrib import admin

from .views import  StudentInsert, AboutUs, Home, posts, Test1,Hellotemplate,Products, blogTest,Contact, Thanks,Postablog

urlpatterns=[

    url(r'^test1/',Test1),
    url(r'^hello/',Hellotemplate),
    url(r'^proddb/',Products),
    url(r'^blogpost/',posts),
    url(r'^blogtest/',blogTest),
    url(r'^contact/',Contact),
    url(r'^thanks/',Thanks,name='thankyou'),
    url(r'^studentinsert/',StudentInsert),
    url(r'^postblogs/',Postablog,name='postblogs'),
    url(r'^$',Home,name='home'),
    url(r'^/aboutus',AboutUs,name='aboutus'),
]
