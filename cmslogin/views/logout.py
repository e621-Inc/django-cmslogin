from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views.generic import View

from ..forms import CMSLogoutForm


class LogoutView(View):

    def post(self, request, *args, **kwargs):
        form = CMSLogoutForm(request, data=request.POST)
        if form.is_valid():
            form.logout()
            return HttpResponseRedirect(form.get_success_url())
        return HttpResponseRedirect(form.get_error_url())
