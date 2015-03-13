from django.conf.urls import url
from snippets import views

urlpatterns = [
	url(r'^snippets/$', views.snippet_list),
	url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^users/$', views.user_list),
    url(r'^users/register', views.user_register),
    url(r'^users/login', views.user_login),
    url(r'^users/add/home',views.user_add_home),
    url(r'^users/add/work', views.user_add_work),
    url(r'^creditcards/$', views.credit_card_list),
    url(r'^creditcards/register', views.credit_card_register),
    url(r'^drivers/$', views.driver_list),
    url(r'^drivers/login', views.driver_login),
    url(r'^drivers/register', views.driver_register),
    url(r'^drivers/get/nearby', views.driver_get_nearby),
    url(r'^drivers/position/update', views.driver_update_position),
    url(r'^uber/request/send', views.send_uber_request),
    url(r'^uber/request/get',views.get_uber_request),
    url(r'^uber/request/$', views.list_uber_request),
    url(r'^uber/request/accept', views.accept_uber_request),
    url(r'^uber/request/pending', views.pending_uber_request),
    url(r'^uber/ride/$', views.ride_list),
]