from __future__ import unicode_literals

from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


from cms.plugin_base import CMSPluginBase

from ..forms import CMSLoginForm, CMSLogoutForm
from ..models import CMSLogin


class CMSLoginPluginForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = CMSLogin
        labels = {}
        widgets = {}


class CMSLoginPlugin(CMSPluginBase):

    cache = False
    form = CMSLoginPluginForm
    model = CMSLogin
    module = _('Content')
    name = _('Login form')
    render_template = 'cmslogin/plugin_cmslogin.html'

    def render(self, context, instance, placeholder):
        login_form = self.get_login_form(instance, context.get('request'))
        logout_form = self.get_logout_form(instance, context.get('request'))
        context.update({
            'object': instance,
            'login_form': login_form,
            'logout_form': logout_form,
            'login_url': reverse('cmslogin-login'),
            'logout_url': reverse('cmslogin-logout'),
            'placeholder': placeholder,
        })
        return context

    def get_login_form(self, obj, request):
        data = None
        if request.session.get('cmslogin'):
            data = request.session['cmslogin'].get('data')
            del request.session['cmslogin']
        initial = {
            'error_url': obj.get_error_url(),
            'success_url': obj.get_success_url(),
        }
        form = CMSLoginForm(request, data=data, initial=initial)
        if form.is_user():
            return None
        return form

    def get_logout_form(self, obj, request):
        initial = {
            'error_url': obj.get_error_url(),
            'success_url': obj.get_success_url(),
        }
        return CMSLogoutForm(request, data=None, initial=initial)
