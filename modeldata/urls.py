from django.conf.urls import url
from modeldata import views

urlpatterns = [
    url(r'^items/$', views.item_list),
    #url(r'^items/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
