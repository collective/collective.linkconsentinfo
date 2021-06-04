# -*- coding: utf-8 -*-

from collective.linkconsentinfo import _
from plone.app.contenttypes.browser.link_redirect_view import (
    LinkRedirectView,
    NON_REDIRECTABLE_URL_SCHEMES,
    NON_RESOLVABLE_URL_SCHEMES,
)
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import ITypesSchema
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility

import six


class LinkConsentInfo(LinkRedirectView):
    """ Subclass LinkRedirectView to inject link consent switch and template
    """

    index = ViewPageTemplateFile("link_consent_info.pt")

    def __call__(self):
        """Redirect to the Link target URL, if and only if:
         - redirect_links property is enabled in
           configuration registry
         - the link is of a redirectable type (no mailto:, etc)
         - enable_consent_info is False
         - AND current user doesn't have permission to edit the Link"""

        context = self.context
        mtool = getToolByName(context, "portal_membership")

        registry = getUtility(IRegistry)
        settings = registry.forInterface(ITypesSchema, prefix="plone")
        redirect_links = settings.redirect_links

        can_edit = mtool.checkPermission("Modify portal content", context)
        redirect_links = (
            redirect_links
            and not context.enable_consent_info
            and not self._url_uses_scheme(NON_REDIRECTABLE_URL_SCHEMES)
        )

        if redirect_links and not can_edit:
            target_url = self.absolute_target_url()
            if six.PY2:
                target_url = target_url.encode("utf-8")
            return self.request.RESPONSE.redirect(target_url)
        else:
            return self.index()