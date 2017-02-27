from django.conf.urls import url, include
from main import views

urlpatterns = [
    url(r'^id_(?P<pk>[0-9])/$', views.IndexView.as_view(), name='user_page'),
    url(r'^login/$', views.LoginView.as_view(), name='login_page'),
    url(r'^login_act/$', views.login_act, name='login_act'),
    url(r'^logout/$', views.logout_act, name="logout_act"),
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration_view'),
    url(r'^registration_act/$', views.registration_act, name='registration_act')
]