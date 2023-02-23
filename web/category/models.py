from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    INACTIVE = 0
    ACTIVE = 1
    STATUS_CHOICES = [
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active'))
    ]
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name=_('Main Category'))
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=INACTIVE, verbose_name=_('Status'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return self.name

    def get_parent_name(self):
        return self.parent.name if self.parent else ''

    def get_status_name(self):
        return dict(self.STATUS_CHOICES).get(self.status)