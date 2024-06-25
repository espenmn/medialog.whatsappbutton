# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import medialog.whatsappbutton


class MedialogWhatsappbuttonLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.whatsappbutton)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.whatsappbutton:default')


MEDIALOG_WHATSAPPBUTTON_FIXTURE = MedialogWhatsappbuttonLayer()


MEDIALOG_WHATSAPPBUTTON_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_WHATSAPPBUTTON_FIXTURE,),
    name='MedialogWhatsappbuttonLayer:IntegrationTesting',
)


MEDIALOG_WHATSAPPBUTTON_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_WHATSAPPBUTTON_FIXTURE,),
    name='MedialogWhatsappbuttonLayer:FunctionalTesting',
)


MEDIALOG_WHATSAPPBUTTON_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_WHATSAPPBUTTON_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MedialogWhatsappbuttonLayer:AcceptanceTesting',
)
