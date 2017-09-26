"""pustakalaya URL Configuration

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

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

urlpatterns = [
    # Static pages
    # about page http://pustakalaya.org/about/
    url(
        r'^about/$',
        cache_page(60 * 15)(TemplateView.as_view(template_name="static_pages/about.html")),
        name="about"
    ),
    # Feedback page
    # /feedback/
    url(
        r'^feedback/$',
        cache_page(60 * 15)(TemplateView.as_view(template_name="static_pages/feedback.html")),
        name="feedback"
    ),
    # Help page
    # /help/
    url(
        r'^help/$', TemplateView.as_view(template_name="static_pages/help.html"),
        name="help"
    ),

    # Django admin
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),

    # Dashboard app
    url(r'^dashboard/', include('pustakalaya_apps.dashboard.urls')),

    # Document App

    # Video App

    # Audio App

    # Wiki App

    # Homepage
    url(r'^', include('pustakalaya_apps.core.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
