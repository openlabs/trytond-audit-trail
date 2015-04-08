# -*- coding: utf-8 -*-
"""
    tests/test_audit_trail.py

    :copyright: (C) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""


class TestAuditTrail:

    def test_views(self, install_module):
        "Test all tryton views"

        from trytond.tests.test_tryton import test_view
        test_view('audit_trail')

    def test_depends(self, install_module):
        "Test missing depends on fields"

        from trytond.tests.test_tryton import test_depends
        test_depends()
