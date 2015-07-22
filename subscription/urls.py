from django.conf.urls import patterns, url
from .views import home


urlpatterns = patterns('subscription.urls',
    url(r'^$', home, name='home'),
)