from django.conf.urls import url
from darasa import views

urlpatterns = [
	url(r'^$',views.api_root),
    url(r'^students/$', views.ListCreateStudent.as_view(),name='student-list'),
    url(r'^students/(?P<pk>[0-9]+)/$', views.DetailStudent.as_view()),
    url(r'^teachers/$', views.ListCreateTeacher.as_view(),name='teacher-list'),
	url(r'^teachers/(?P<pk>[0-9]+)/$', views.DetailTeacher.as_view()),
]
