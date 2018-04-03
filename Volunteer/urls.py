from django.conf.urls import url
from . import views
from .views import profile, event_reg, regd_events, event_unreg, feedback

urlpatterns = [
    url(r'^profile/$', profile, name='profile'),
    url(r'^(?P<event_id>[0-9]+)/(?P<user_id>[0-9]+)/regevent$', event_reg, name='event-register'),
    url(r'^(?P<event_id>[0-9]+)/(?P<user_id>[0-9]+)/unregevent$', event_unreg, name='event-unregister'),
    url(r'^profile/regevents$', regd_events, name='registered-events'),
    url(r'^profile/(?P<event_id>[0-9]+)/feedback$', feedback, name= 'feedback'),

]
