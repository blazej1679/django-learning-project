from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    path('admin', admin.site.urls),
    #url(r'^$', include('learning_logs.urls'), name='learning_logs'),
    path('', include('learning_logs.urls'), name='learning_logs'),

    path('users/', include('users.urls'), name='users'),
]
