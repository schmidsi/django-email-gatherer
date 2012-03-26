from django.conf.urls.defaults import *
from django.views.generic import CreateView

from .models import GatheredEmail


urlpatterns = patterns('',
    url(r'', CreateView.as_view(model=GatheredEmail, success_url='/?new-email=%(email)s'))
)