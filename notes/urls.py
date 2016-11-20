
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/$', views.CateView.as_view(), name='cate'),
    url(r'^add/$', views.AddView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)$', views.EditView.as_view(), name='edit'),
    url(r'^note/(?P<pk>\d+)$', views.NoteDetailView.as_view(), name='note'),
    url(r'^delete/(?P<pk>\d+)$', views.NoteDeleteView.as_view(), name='delete')
]
