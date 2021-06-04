# -*- coding: utf-8 -*-

from collective.linkconsentinfo import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class ILinkConsentInfoBehaviorMarker(Interface):
    pass


@provider(IFormFieldProvider)
class ILinkConsentInfoBehavior(model.Schema):
    """
    """

    project = schema.TextLine(
        title=_(u'Project'),
        description=_(u'Give in a project name'),
        required=False,
    )


@implementer(ILinkConsentInfoBehavior)
@adapter(ILinkConsentInfoBehaviorMarker)
class LinkConsentInfoBehavior(object):
    def __init__(self, context):
        self.context = context

    @property
    def project(self):
        if safe_hasattr(self.context, 'project'):
            return self.context.project
        return None

    @project.setter
    def project(self, value):
        self.context.project = value
