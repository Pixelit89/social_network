from django.conf.urls import url, include
from main import views

urlpatterns = [
    url(r'^(?P<pk>[0-9])$', views.IndexView.as_view())
]