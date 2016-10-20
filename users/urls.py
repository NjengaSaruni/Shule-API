from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^users/$', views.UserListCreateView.as_view(),name='user-list'),
    url(r'^users/(?P<pk>[^/]+)/$', views.UserDetailView.as_view(),name='user-detail')

]