"""employee_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.utils.translation import ugettext as _

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Django-Select2
    url(r'^select2/', include('django_select2.urls')),
    #RestAPI
    url(r'^employee/', include('modules.employees.urls', namespace='employee'))
]

admin.site.site_header = _(u'Employee Manager')
admin.site.index_title = _(u'Luizalabs Employee Manager')
admin.site.site_title = _(u'Luizalabs Employee Manager')
