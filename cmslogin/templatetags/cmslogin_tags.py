from __future__ import unicode_literals


from django import template
from django.core.urlresolvers import reverse

from ..forms import CMSLoginForm, CMSLogoutForm


register = template.Library()


# TODO create reusable code, quick and dirty atm !!!

@register.inclusion_tag('cmslogin/tag_loginout.html', takes_context=True)
def cmslogin_loginout(context, **kwargs):
    request = context.get('request')
    login_form = None
    logout_form = None
    user = getattr(request, 'user', None)
    print user.is_active
    if not getattr(user, 'is_active', False):
        data = None
        if request.session.get('cmslogin'):
            data = request.session['cmslogin'].get('data')
            del request.session['cmslogin']
        initial = {
            'error_url': request.get_full_path(),
            'success_url': request.get_full_path(),
        }
        login_form = CMSLoginForm(request, data=data, initial=initial)
        if login_form.is_user():
            login_form = None
    else:
        initial = {
            'error_url': request.get_full_path(),
            'success_url': request.get_full_path(),
        }
        logout_form = CMSLogoutForm(request, data=None, initial=initial)
    return {
        'login_form': login_form,
        'logout_form': logout_form,
        'login_url': reverse('cmslogin-login'),
        'logout_url': reverse('cmslogin-logout'),
    }


@register.inclusion_tag('cmslogin/tag_login.html', takes_context=True)
def cmslogin_login(context, **kwargs):
    request = context.get('request')
    data = None
    if request.session.get('cmslogin'):
        data = request.session['cmslogin'].get('data')
        del request.session['cmslogin']
    initial = {
        'error_url': request.get_full_path(),
        'success_url': request.get_full_path(),
    }
    form = CMSLoginForm(request, data=data, initial=initial)
    if form.is_user():
        form = None
    return {
        'login_form': form,
        'login_url': reverse('cmslogin-login'),
    }


@register.inclusion_tag('cmslogin/tag_logout.html', takes_context=True)
def cmslogin_logout(context, **kwargs):
    request = context.get('request')
    initial = {
        'error_url': request.get_full_path(),
        'success_url': request.get_full_path(),
    }
    form = CMSLogoutForm(request, data=None, initial=initial)
    if not form.is_user():
        form = None
    return {
        'logout_form': form,
        'logout_url': reverse('cmslogin-logout'),
    }
