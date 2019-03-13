from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views.generic import View

from ..forms import CMSLoginForm


class LoginView(View):

    def post(self, request, *args, **kwargs):
        form = CMSLoginForm(request, data=request.POST)

        if form.is_valid():
            return HttpResponseRedirect(form.get_success_url())
        request.session['cmslogin'] = {
            'error': True,
            'data': request.POST,
            'errors': form.errors,
        }
        return HttpResponseRedirect(form.get_error_url())
