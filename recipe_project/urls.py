from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from family_recipes_app.views import index, about
 
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^admin/', admin.site.urls),
]
