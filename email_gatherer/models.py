from django import forms
from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .utils import get_object


class GatheredEmail(models.Model):
    """
    Simple base model. The only field, every possible email gathering system has in common is: email.
    But it is extensible. So check the extensions or write your own (and make a pull request).
    """
    
    email = models.EmailField(help_text=_('The gathered email.'))

    class Meta:
        verbose_name = _('Gathered Email')
        verbose_name_plural = _('Gathered Emails')
    
    # all extensions are listed here
    _extensions = set()
    
    @classmethod
    def register_extension(cls, register_fn):
        #from .admin import GatheredEmailAdmin
        """
        actually register an extension
        """
        register_fn(cls, GatheredEmailAdmin)
    
    @classmethod
    def register_extensions(cls, *extensions):
        """
        Register all extensions passed as arguments.

        Extensions should be specified as a string to the python module
        containing the extension. If it is a bundled extension,
        you do not need to specify the full python module path -- only
        specifying the last part (f.e. ``'created'`` or ``'user_agent'``) is
        sufficient.
        """

        here = cls.__module__.split('.')[:-1]

        paths = [
            'email_gatherer.extensions',
            ]

        for ext in extensions:
            if ext in cls._extensions:
                continue

            fn = None
            if isinstance(ext, basestring):
                try:
                    fn = get_object(ext + '.register')
                except ImportError:
                    for path in paths:
                        try:
                            fn = get_object('%s.%s.register' % (path, ext))
                            if fn:
                                break
                        except ImportError:
                            pass

                if not fn:
                    raise ImproperlyConfigured, '%s is not a valid extension for %s' % (
                        ext, cls.__name__)

            # Not a string, maybe a callable?
            elif hasattr(ext, '__call__'):
                fn = ext

            # Take our chances and just try to access "register"
            else:
                fn = ext.register

            cls.register_extension(fn)
            cls._extensions.add(ext)


class GatheredEmailAdmin(admin.ModelAdmin):
    list_display=['email',]


class GatheredEmailForm(forms.ModelForm):
    class Meta:
        model = GatheredEmail
