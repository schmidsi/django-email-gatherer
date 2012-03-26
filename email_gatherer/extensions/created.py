from datetime import datetime
from django.db import models


def register(cls, admin_cls):
    cls.add_to_class('created', models.DateTimeField(auto_now_add=True, default=datetime.now))
    admin_cls.list_display += ('created',)
