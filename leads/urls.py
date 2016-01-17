from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.LeadsList.as_view(), name='leads-list'),
    url(r'^create/$', views.TourLeadCreateView.as_view(), name='create'),
    url(r'^all_tours/$', views.TourLeadListView.as_view(), name='tours'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.TourLeadEditView.as_view(), name='edit_tour'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.TourLeadDeleteView.as_view(), name='delete'),
    url(r'^tour/(?P<pk>[0-9]+)/$', views.TourLeadDetailView.as_view(), name='tour'),
)
