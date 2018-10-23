"""web_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import view
from django.conf.urls import include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', view.hello),
    url(r'^get_req/', view.http_get),
    url(r'^post_req/', view.http_post),
    url(r'^py_json/', view.py_json),
    url(r'^md5Encrypt/', view.md5Encrypt),
    url(r'^time_date/', view.date_differ),
    url(r'^deal_string/', view.deal_string),
#     url(r'^articles/comments/', include('django_comments.urls')),
    url(r'^blog/comments/', include('fluent_comments.urls')),



]

# urlpatterns += ('',
#     url(r'^articles/comments/', include('django_comments.urls')),
# )
