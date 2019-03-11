from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=255)
    done = models.BooleanField(_("Done"), default=False)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos")

    def __unicode__(self):
        return smart_unicode(self.name)
