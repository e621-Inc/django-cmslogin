from __future__ import unicode_literals

from cms.plugin_pool import plugin_pool

from .cmslogin import CMSLoginPlugin
from .cmslogout import CMSLogoutPlugin


plugin_pool.register_plugin(CMSLoginPlugin)
plugin_pool.register_plugin(CMSLogoutPlugin)
