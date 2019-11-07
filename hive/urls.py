from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin


from .views import emailView, successView




urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^student$', views.studentApply, name='studentApply'),
    
   
    url(r'^business$', views. businessEntApply, name='businessEntApply'),
    url(r'^academic$', views.academicApply, name='academicApply'),
    url(r'^government$', views. governmentApply, name='governmentApply'),
    url(r'^start$', views.start, name='start'),
    url(r'^about$', views.about, name='about'),
    url(r'^solutions$', views.solutions, name='solutions'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^solution$', views.solution1, name='solution'),
    url(r'^enterpreneurship$', views.enterpreneurship, name='enterpreurship'), 
    url('email/', emailView, name='email'),
    url('success/', successView, name='success'),
    url(r'^news$', views.news_today, name='newsToday'),
    url('team/', views.team, name = 'team'),
    url(r'^comment$', views.comment, name='comment'),
    url(r'^comments$', views.voir_comment, name='see'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)