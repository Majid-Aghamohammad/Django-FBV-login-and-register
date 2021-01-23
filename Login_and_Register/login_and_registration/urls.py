from django.conf.urls import url
from .views import home_page,singup_page,registred_page,user_login,sucsse_page,logout_page
################################################################################
urlpatterns = [
    url(r'^$',home_page,name='home'),
    url(r'register/',singup_page),
    url(r'login/',user_login,name='user_login'),
    url(r'registred/',registred_page,name='registred'),
    url(r'sucsse/',sucsse_page),
    url(r'logout/',logout_page ,name='logout'),
    ]
