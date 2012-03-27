from django.views.generic import CreateView

from .models import GatheredEmail


class GatheredEmailView(CreateView):
    model = GatheredEmail
