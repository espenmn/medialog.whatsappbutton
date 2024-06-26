# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api


class WhatsAppViewlet(ViewletBase):

    def update(self):
        self.phone = self.get_phone()
        self.color = self.get_color()

    def get_phone(self):
        phone = api.portal.get_registry_record('medialog.whatsappbutton.interfaces.ISettings.phone', default='')
        return phone

    def get_color(self):
        color = api.portal.get_registry_record('medialog.whatsappbutton.interfaces.ISettings.color', default='#123456')
        return color

    def index(self):
        return super(WhatsAppViewlet, self).render()
