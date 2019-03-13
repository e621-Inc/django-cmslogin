from __future__ import unicode_literals

from cms.plugin_pool import plugin_pool

from .cmslogin import CMSLoginPlugin


plugin_pool.register_plugin(CMSLoginPlugin)
