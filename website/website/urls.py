from django.conf.urls import url,include

from django.contrib import admin
from blog.views import Products,Mobiles,Books

from friend.views import BestFriend,NormalFriend


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pro/',Products),
    url(r'^mob/',Mobiles),
    url(r'^book/',Books),
    url(r'^bestfriend/',BestFriend),
    url(r'^normalfriend/',NormalFriend),
    url(r'^test/',include('testapp.urls')),
    url(r'^blog/',include('blog.urls')),
    url(r'^friend/',include('friend.urls')),
]
