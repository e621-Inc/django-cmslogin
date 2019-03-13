from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PageField


@python_2_unicode_compatible
class CMSLogin(CMSPlugin):

    name = models.CharField(
        max_length=255,
        default='',
        verbose_name=_('Title')
    )
    cms_page = PageField(
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Success target'),
        help_text=_(
            'If left empty the user stays on the current page.'
        ),
    )
    show_logout = models.BooleanField(
        default=True,
        verbose_name=_('Show logout'),
        help_text=_(
            'If the user is allready logged-in: '
            ' if checked a log out button is shown.'
            ' else the plugin is invisible.'
        ),
    )

    @property
    def slug(self):
        return '{}'.format(slugify(self.name))

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        if self.placeholder.page:
            return '{}#{}'.format(
                self.placeholder.page.get_absolute_url(),
                self.slug,
            )
        return ''

    def get_error_url(self, request=None):
        return self.get_absolute_url()

    def get_success_url(self, request=None):
        page = self.cms_page or self.placeholder.page
        if not page:
            page = getattr(request, 'current_page', None)
        if page:
            return page.get_absolute_url()
        return ''
