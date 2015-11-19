"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.dates import ArchiveIndexView
from blog2.views import ParutionDetailView
#from blog.views import ArticleDayArchiveView
from blog2.views import ParutionListView
#from blog.views import ArticleDetailView
#from blog.models import Article


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^testeur$','testeur.views.home',name="testeur"),

    #supplément simple auth
    #url(r'^login/$','myauth.views.mylogin',name="login"),

    #archives
    #url(r'^archive/$',ArchiveIndexView.as_view(model=Article, date_field="date"),name="article_archive"),
    #url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$',ArticleDayArchiveView.as_view(),name="archive_day"),

    #supplément accounts
    #url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^accounts/srvup$','accounts.views.srvup',name='srvup'),

    #supplément blogdef
    url(r'^$','blogdef.views.publication_list',name="test"),#menu
    url(r'^parutions/$','blogdef.views.publication_list',name="liste"),
    url(r'^parution/(?P<pk>[\d]+)/$','blogdef.views.publication_detail' , name='parution-detail'),

    #supplément blog2
    # url(r'^$',ParutionListView.as_view(),name="test"), #menu
    # url(r'^parutions/$', ParutionListView.as_view(),name="liste"),
    # url(r'^parution/(?P<pk>[\d]+)/$', ParutionDetailView.as_view(), name='parution-detail'),

    #Fait parti du menu
    url(r'^message','message.views.myMessage',name="monMessage"),
    url(r'^login/$','accounts.views.mylogin',name="login"),
    url(r'^register/$','accounts.views.register',name="register"),
    url(r'^logout/$','accounts.views.mylogout',name="logout"),


]
