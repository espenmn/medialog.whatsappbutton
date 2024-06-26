# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider


from zope import schema
from zope.interface import alsoProvides
from plone.supermodel import model
 


class IMedialogWhatsappbuttonLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

    

class ISettings(model.Schema):
    """Adds settings to medialog.controlpanel
    """

    model.fieldset(
        'whatsapp_menu',
        label=(u'WhatsAppButton'),
        fields=[
            'phone', 
            'color',
            ],
        )

     
    phone =  schema.Int(
        title="phone", 
    )

    color =  schema.TextLine(
        title="Button Color", 
    )



alsoProvides(ISettings, IMedialogControlpanelSettingsProvider)