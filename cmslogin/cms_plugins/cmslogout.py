from __future__ import unicode_literals

from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


from cms.plugin_base import CMSPluginBase

from ..forms import CMSLogoutForm
from ..models import CMSLogout


class CMSLogoutPluginForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = CMSLogout
        labels = {}
        widgets = {}


class CMSLogoutPlugin(CMSPluginBase):

    cache = False
    form = CMSLogoutPluginForm
    model = CMSLogout
    module = _('Content')
    name = _('Logout button')
    render_template = 'cmslogin/plugin_cmslogout.html'

    def render(self, context, instance, placeholder):
        logout_form = self.get_logout_form(instance, context.get('request'))
        context.update({
            'object': instance,
            'logout_form': logout_form,
            'logout_url': reverse('cmslogin-logout'),
            'placeholder': placeholder,
        })
        return context

    def get_logout_form(self, obj, request):
        initial = {
            'error_url': obj.get_error_url(),
            'success_url': obj.get_success_url(),
        }
        form = CMSLogoutForm(request, data=None, initial=initial)
        if form.is_user():
            return form
        return None
